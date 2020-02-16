from django.db import models
from django.utils import timezone
from core import models as core_models

# Create your models here.
class Reservation(core_models.TimeStampedModel):
    
    """ Reservation Model Definition """
    
    STATUS_PENDING = "pending"
    STATUS_CONFIRMED = "confirmed"
    STATUS_CANCELED = "canceled"
    
    STATUS_CHOICES = (
        (STATUS_PENDING, "pending"),
        (STATUS_CONFIRMED, "confirmed"),
        (STATUS_CANCELED, "canceled"),
    )

    status = models.CharField(
        max_length=12, choices=STATUS_CHOICES, default=STATUS_PENDING
        )
    check_in = models.DateField()
    check_out = models.DateField()
    guest = models.ForeignKey("users.User",related_name="reservations" , on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room",related_name="reservations" , on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.room} - {self.check_in}"
    
    def in_progress(self):
        now = timezone.now().date()
        return now >= self.check_in and now <= self.check_out
    
    in_progress.boolean = True # 이걸로 글자형태가 아닌 아이콘으로 바꼈을 것이다.
    
    def is_finished(self):
        now = timezone.now().date()
        return now > self.check_out
    
    is_finished.boolean = True