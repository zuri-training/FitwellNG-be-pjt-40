from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from .forms import CustomUserChangeForm, CustomUserCreationForm

# Register your models here.


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    model = User
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'dob', 'weight', 'height', 'nationality', 'state')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {
         'fields': ('dob', 'weight', 'height', 'nationality', 'state')}),
        ('Security', {'fields': ('security', 'security_answer')})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'dob', 'weight', 'height', 'nationality', 'state')}
         ),
    )

    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
