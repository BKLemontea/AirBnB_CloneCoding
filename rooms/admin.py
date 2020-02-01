from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.RoomType, models.Facilitiy, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    pass

@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    
    """ Room Admin Definition """
    
    fieldsets = (
        (
            "Basic Info",
            {
                "fields": (
                    "name",
                    "description",
                    "country",
                    "address",
                    "price"
                )
            },
        ),
        (
            "Times",
            {
                "fields": (
                    "check_in",
                    "check_out",
                    "instant_book"
                )
            },
        ),
        (
            "Spaces",
            {
                "fields": (
                    "guests", 
                    "beds", 
                    "bedrooms", 
                    "baths"
                )
            },
        ),
        (
            "More About the Space",
            {
                "classes": (
                    "collapse",    
                ),
                "fields": (
                    "amenities",
                    "facilities",
                    "house_rule"
                )
            },
        ), 
        (
            "Last Details",
            {
                "fields": (
                    "host",
                )
            },
        ),
    )
    
    # ordering = ("name","price","bedrooms",)
    
    list_display = (
        "name", 
        "country", 
        "city", 
        "price", 
        "guests", 
        "beds", 
        "bedrooms", 
        "baths", 
        "check_in", 
        "check_out", 
        "instant_book", 
        "count_amenities",
    )
    
    list_filter = (
        "instant_book", 
        "host__superhost",
        "host__gender",
        "room_type",
        "amenities",
        "facilities",
        "house_rule",
        "city",
        "country",
    )
    
    search_fields = (
        "=city",
        "^host__username",
        )
    
    # 다대다 관계
    filter_horizontal = (
        "amenities",
        "facilities",
        "house_rule",
    )
    
    def count_amenities(self, obj):
        print(obj.amenities.all())
        return "Potato"
    
    count_amenities.short_description = "hello sexy!"

@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    
    """ Photo Admin Definition """
    
    pass