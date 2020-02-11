from django.contrib import admin
from django.utils.html import mark_safe
from . import models

# Register your models here.
@admin.register(models.RoomType, models.Facilitiy, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    list_display = (
        "name",
        "used_by"
    )

    def used_by(self, obj):
        return obj.rooms.count()
    
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
        "count_photos",
        "total_rating"
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
        return obj.amenities.count()
    
    def count_photos(self, obj):
        return obj.photos.count()

@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    
    """ Photo Admin Definition """
    
    list_display = (
        "__str__",
        "get_thumnnail"
    )
    
    def get_thumnnail(self, obj):
        # mark_safe를 사용해야 정상적으로 태그를 사용할 수 있다.
        return mark_safe(f'<img width="50px" src="{obj.file.url}"/>')
    get_thumnnail.short_description = "Thumnnail"