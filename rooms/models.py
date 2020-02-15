from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
# from users import models as user_models

# Create your models here.
class AbstractItem(core_models.TimeStampedModel):
    
    """ Abstract Item """
    
    name = models.CharField(max_length=80)
    
    class Meta:
        abstract = True
        
    def __str__(self):
        return self.name
    
class RoomType(AbstractItem):
    
    """ RoomType Model Definition """
    
    class Meta:
        # verbose_name 는 뒤에 붙는 s는 유지하고 나머지 문장을 수정함
        # verbose_name_plural 는 s단어까지 포함하여 모두 수정함
        verbose_name = "Room Type" 
        #ordering = ['name'] or ordering = ['created'] 정렬방식을 정할 수 있다.

class Amenity(AbstractItem):
    
    """ Amenity Model Definition """
    
    class Meta:
        verbose_name_plural = "Amenities"

class Facilitiy(AbstractItem):
    
    """ Facilitiy Model Definition """
    
    class Meta:
        verbose_name_plural = "Facilities"

class HouseRule(AbstractItem):
    
    """ HouseRule Model Definition """
    
    class Meta:
        verbose_name = "House Rule"
        
class Photo(core_models.TimeStampedModel):
    
    """ Photo Model Definition """
    
    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to="room_photos") # upload_to는 uploads 폴더안의 어떤 폴더에다가 사진을 업로드 할것인지
    # 가져올 항목을 String 형식으로 하게되면 상하관계가 필요없으며, importing도 할 필요가 없다.
    room = models.ForeignKey("Room",related_name="photos" , on_delete=models.CASCADE)
    
    def __str__(self):
        return self.caption

class Room(core_models.TimeStampedModel):
    
    """ Room Model Definition """
    
    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    # host = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    host = models.ForeignKey("users.User",related_name="rooms" ,on_delete=models.CASCADE) # 다대일의 관계 , CASCADE(폭포수) 연관되어있는 것들을 모두 삭제함
    room_type = models.ForeignKey("RoomType",related_name="rooms" , on_delete=models.SET_NULL, null=True)
    amenities = models.ManyToManyField("Amenity",related_name="rooms" , blank=True) # 다대다의 관계
    facilities = models.ManyToManyField("Facilitiy",related_name="rooms" , blank=True)
    house_rule = models.ManyToManyField("HouseRule",related_name="rooms" , blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.city = str.capitalize(self.city)
        super().save(*args, **kwargs)
    
    def total_rating(self):
        all_reviews = self.reviews.all()
        all_ratings = 0
        if len(all_reviews) > 0:
            for review in all_reviews:
                all_ratings += review.rating_average()
            return round(all_ratings / len(all_reviews), 2)
        return 0