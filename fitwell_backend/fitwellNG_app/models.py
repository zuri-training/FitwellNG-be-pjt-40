from django.db import models
from django.contrib.auth.models import AbstractUser
import os
from .managers import UserManager

# Create your models here.


def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)


class User(AbstractUser):
  
  countries = [
    ('NIG', 'Nigerian'),
  ]
  states = [
    ('KW', 'Kwara')
  ]

  username = None
  first_name = models.CharField('First Name', max_length=64)
  last_name = models.CharField('Last Name', max_length=64)
  email = models.EmailField('Email', unique=True)
  dob = models.DateField('Date of Birth', null=True)
  sex = models.CharField('Sex', choices=[
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Prefer Not To Say')
  ], max_length=50)
  nationality = models.CharField('Country of Origin', choices=countries, max_length=50)
  state = models.CharField(choices=states, max_length=50)
  weight = models.DecimalField('Weight', help_text='Enter your weight in kg', max_digits=5, decimal_places=2)
  height = models.DecimalField('Height', help_text='Enter your height in cm', max_digits=5, decimal_places=2)
  security = models.TextField('Security question',)
  security_answer = models.CharField('Answer', max_length=50)
  image = models.ImageField('Image', null=True, upload_to=get_image_path, default='image\default.png')
  phone_no = models.CharField(max_length=14, null=True)

  USERNAME_FIELD = 'email'
  # [jbadonai] : dob added to REQUIRE_FIELDS because Not a Null value is set for the field.
  REQUIRED_FIELDS = ['phone_no', 'height', 'weight', 'password']
  objects = UserManager()
  
  def __str__(self) -> str:
      return f"{self.first_name} {self.last_name}: {self.email}"