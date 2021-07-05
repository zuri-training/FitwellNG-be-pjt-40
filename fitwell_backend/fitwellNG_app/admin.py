from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class UserAdminConfig(UserAdmin):
    search_field = ('email', 'first_name')     # Search Field
    list_filter = ('email', 'first_name', 'height')    # filter Fields
    ordering = ('-first_name',)     # ordering
    list_display = ('email', 'height', 'weight', 'is_active')   # items to display on the admin home page table
    # category and fields to display for a detail view of a user on the admin page
    fieldsets = (
        ('General',{'fields': ('email', 'first_name', 'last_name')}),
        ('Permission', {'fields': ('is_superuser', 'is_active')}),
        ('Personal', {'fields': ('height', 'weight', 'phone_number')})
    )
    # category and items to display when adding a new user from admin page
    add_fieldsets = (
        ("Login Info", {'classes': 'wide', 'fields':('email','password1')}),
        ("Health Info", {'classes': 'wide', 'fields': ( 'height', 'weight')}),
    )


admin.site.register(User, UserAdminConfig)

