from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class UserAdminConfig(UserAdmin):
    search_field = ('email', 'first_name')     # Search Field
    list_filter = ('email', 'first_name', 'height')    # filter Fields
    ordering = ('-first_name',)     # ordering
    list_display = ('email', 'sex', 'height', 'weight', 'is_active')   # items to display on the admin home page table
    # category and fields to display for a detail view of a user on the admin page
    fieldsets = (
        ('General',{'fields': ('email', 'first_name', 'last_name')}),
        ('Permission', {'fields': ('is_superuser', 'is_active')}),
        ('Personal', {'fields': ('height', 'dob', 'state', 'nationality')})
    )
    # category and items to display when adding a new user from admin page
    add_fieldsets = (
        ("Login Info", {'classes': 'wide', 'fields':('email','password1', 'password2')}),
        ("Health Info", {'classes': 'wide', 'fields': ('dob', 'height', 'weight', 'sex')}),
        ("Security Info", {'classes': 'wide', 'fields': ('security', 'security_answer')}),

    )


# admin.site.register(User, UserAdminConfig)
admin.site.register(User)

