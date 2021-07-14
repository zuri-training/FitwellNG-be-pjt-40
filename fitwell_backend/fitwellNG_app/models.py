from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
import os
from .managers import UserManager
from django.template.defaultfilters import slugify
from django.utils import  timezone


def get_image_path(instance, filename):
    return os.path.join('image', str(instance.id), filename)


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
    security = models.TextField('Security question', )
    security_answer = models.CharField('Answer', max_length=50)
    image = models.ImageField('Image', null=True, upload_to=get_image_path, default='image\default.png')
    phone_no = models.CharField(max_length=14, null=True)
    # meal_plan = models.ManyToManyField(MealPlan)

    USERNAME_FIELD = 'email'
    # [jbadonai] : dob added to REQUIRE_FIELDS because Not a Null value is set for the field.
    REQUIRED_FIELDS = ['phone_no', 'height', 'weight']
    objects = UserManager()

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}: {self.email}"

#   ******************************************************************************

class BreakfastLIst(models.Model):
    class Meta:
        abstract = True
    breakfast = models.CharField(max_length=500, help_text="The meal")
    about_breakfast = models.TextField(help_text="About the meal; e.g. nutritional info or how it's prepared")
    breakfast_calories = models.IntegerField(default=0)
    breakfast_meal_time = models.TimeField(null=True)

    def __str__(self):
        return self.breakfast


class LunchList(models.Model):
    class Meta:
        abstract = True
    lunch = models.CharField(max_length=500, help_text="The meal")
    about_lunch = models.TextField(help_text="About the meal; e.g. nutritional info or how it's prepared")
    lunch_calories = models.IntegerField(default=0)
    lunch_meal_time = models.TimeField(null=True)

    def __str__(self):
        return self.lunch


class DinnerList(models.Model):
    class Meta:
        abstract = True
    dinner = models.CharField(max_length=500, help_text="The meal")
    about_dinner = models.TextField(help_text="About the meal; e.g. nutritional info or how it's prepared")
    dinner_calories = models.IntegerField(default=0)
    dinner_meal_time = models.TimeField(null=True)

    def __str__(self):
        return self.dinner


class DayTable(models.Model):
    class Meta:
        abstract = True
    day = models.IntegerField(help_text="specify day no. e.g day 1 out of 30 days plan")

    def __str__(self):
        return self.day


class MealLists(DayTable, BreakfastLIst, LunchList, DinnerList):
    '''
    Each day meal Plan is created here.
    '''

    name = models.CharField(max_length=300, help_text="Meal plan name e.g. weight shred. Must be repeated for each day in the plan")
    meal_time = models.TimeField(default=timezone.now)
    # calories_intake = models.IntegerField(help_text="calories provided by the meal")
    category = models.CharField(max_length=300, help_text="category of this plan may be similar to name e.g weight loss. Must be repeated for each day in the plan")

    def __str__(self):
        return f"{self.name} - day {self.day}"


class MealPlans(models.Model):
    '''
    This keeps the  record of each user that has signed up for meal plan and what they signed up for.
    '''
    user = models.OneToOneField(get_user_model(), primary_key=True, on_delete=models.CASCADE)
    start_date = models.DateField(null=True)
    active = models.BooleanField(default=False)
    plan_name = models.ForeignKey(MealLists, on_delete=models.CASCADE)

    def __str__(self):
        return self.plan_name


#   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

class Routine(models.Model):
    routine_name = models.CharField(max_length=200, help_text="squats, Jumping-Jack, etc")
    description = models.TextField(help_text="How is it being done?")
    repetition_no = models.IntegerField(help_text="Expected number of repetition daily")
    repetition_achieved_today = models.IntegerField(null=True, default=0, blank=True)
    repetition_achieved_total = models.IntegerField(null=True, default=0, blank=True)

    def __str__(self):
        return self.routine_name


class WorkoutPlanList(models.Model):
    plan = models.CharField(max_length=200, help_text="Beginners, Intermediate, Expert...")
    duration = models.IntegerField(help_text="weeks")
    daily_duration = models.IntegerField(help_text="Time in Mins to spend daily")
    time_spent_today = models.IntegerField(help_text="In Minutes", null=True, default=0, blank=True)
    time_spent_total = models.IntegerField(help_text="In Minutes", null=True, default=0, blank=True)
    routines = models.ManyToManyField(Routine)

    def __str__(self):
        return self.plan


class WorkoutPlan(models.Model):
    '''
       This keeps the  record of each user that has signed up for meal plan and what they signed up for.
       '''
    user = models.OneToOneField(get_user_model(), primary_key=True, on_delete=models.CASCADE)
    workout_plan = models.ForeignKey(WorkoutPlanList, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.email} -- {self.workout_plan.plan}"

    def slug(self):
        return slugify(self.workout_plan.plan)



