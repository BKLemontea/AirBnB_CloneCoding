from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.RoomType, models.Facilitiy, models.Amenity, models.HouseRule)
class RoomAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    pass

@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    
    """ Room Admin Definition """
    
    pass

@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    
    """ Photo Admin Definition """
    
    pass