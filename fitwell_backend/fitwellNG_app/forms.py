from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'dob', 'first_name', 'last_name', 'sex', 'nationality', 'weight', 'height', 'security', 'security_answer', 'phone']


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'
