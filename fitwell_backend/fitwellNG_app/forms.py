from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from .models import User


class LoginForm1(AuthenticationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        field = ['email', 'password']


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.PasswordInput()
