from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from .models import User

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
# from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField

# User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    # def clean_password2(self):
    #     password1 = self.cleaned_data.get('password1')
    #     password2 = self.cleaned_data.get('password2')
    #     if password1 and password2:
    #         if password1 != password2:
    #             raise forms.ValidationError(_("The two password fields didn't match.[][]"))
    #     return password2

    class Meta:
        model = User
        # fields = '__all__'
        fields = ['email', 'password1', 'password2', 'dob', 'first_name', 'last_name', 'sex', 'nationality', 'weight', 'height', 'security', 'security_answer']


class LoginForm1(AuthenticationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        field = ['email', 'password']


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.PasswordInput()
