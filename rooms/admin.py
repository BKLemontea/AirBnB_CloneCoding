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

# Inline Admin은 admin 안데 또다른 admin을 넣는 방법이다.
class PhotoInline(admin.TabularInline):
# class PhotoInline(admin.StackedInline):
    model = models.Photo

@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    
    """ Room Admin Definition """
    
    inlines= (PhotoInline,)
    
    fieldsets = (
        (
            "Basic Info",
            {
                "fields": (
                    "name",
                    "description",
                    "country",
                    "city",
                    "address",
                    "price",
                    "room_type",
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
    
    # 사용자가 많아짐에 따라 리스트가 엄청 길어질건데 
    # raw_id_fields는 user admin을 사용하여 host를 검색할 수 있게 해준다.
    raw_id_fields =(
        "host",
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
    
    #def save_model(self, request, obj, form, change):
    #    send_mail()
    #    super().save_model(request, obj, form, change)
    
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