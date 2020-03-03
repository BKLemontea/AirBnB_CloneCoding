from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.
@admin.register(models.User) #decorator
class CustomUserAdmin(UserAdmin):
    """ Custom User Admin """
    
    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields" : (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            }
        ),
    )
    
    list_filter = UserAdmin.list_filter + (
        "superhost",
    )
    
    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "language",
        "currency",
        "superhost",
        "is_staff",
        "is_superuser",
        "email_verified",
        "email_secret",
    )

"""
class CustomUserAdmin(admin.ModelAdmin):
    
    #Custom User Admin
    
    # User페이지에서 Table명을 바꿔주고 해당 옵션을 보여줌.
    list_display = ("username","email", "gender", "language", "currency", "superhost")
    
    # 해당 필드의 필터를 보여줌.
    list_filter = ("language","currency","superhost",)
"""

"""
둘다 같음
@admin.register(models.User) 클래스 위에 있어야함
admin.site.register(models.User, CustomUserAdmin)
"""
