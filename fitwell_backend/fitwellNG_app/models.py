from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import UserManager

# Create your models here.

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
  dob = models.DateField('Date of Birth')
  sex = models.CharField('Sex', choices=[
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Prefer Not To Say')
  ], max_length=1)
  nationality = models.CharField('Country of Origin', choices=countries, max_length=3)
  state = models.CharField(choices=states, max_length=2)
  weight = models.DecimalField('Weight', help_text='Enter your weight in kg', max_digits=5, decimal_places=2)
  height = models.DecimalField('Height', help_text='Enter your height in cm', max_digits=5, decimal_places=2)
  security = models.TextField('Security question',)
  security_answer = models.CharField('Answer', max_length=50)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['dob', 'sex', 'height', 'weight', 'security', 'security_answer']
  objects = UserManager()
  
  def __str__(self) -> str:
      return f"{self.first_name} {self.last_name}: {self.email}"