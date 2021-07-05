from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import UserManager

# Create your models here.

class User(AbstractUser):
  username = None
  first_name = models.CharField('First Name', max_length=64)
  last_name = models.CharField('Last Name', max_length=64)
  email = models.EmailField('Email', unique=True)
  phone_number = models.IntegerField()
  weight = models.DecimalField('Weight', help_text='Enter your weight in kg', max_digits=5, decimal_places=2)
  height = models.DecimalField('Height', help_text='Enter your height in cm', max_digits=5, decimal_places=2)
  image = models.ImageField('Image', null=True)

  USERNAME_FIELD = 'email'
  # [jbadonai] : dob added to REQUIRE_FIELDS because Not a Null value is set for the field.
  REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number', 'height', 'weight']
  objects = UserManager()
  
  def __str__(self) -> str:
      return f"{self.first_name} {self.last_name}: {self.email}"