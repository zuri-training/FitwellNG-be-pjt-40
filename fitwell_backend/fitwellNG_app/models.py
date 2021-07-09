from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
import os
from .managers import UserManager
from django.utils import  timezone


# ==========================
# < MEAL PLAN STARTS HERE >
#
# class Breakfast(models.Model):
#     meal = models.CharField(max_length=200)
#     calories = models.IntegerField(default=0)
#     quantity = models.IntegerField(default=0)
#     how_to_prepare = models.TextField(null=True)
#     where_to_get = models.TextField(null=True)
#     image = models.ImageField(upload_to="photos/foods", default="image/default_food.jpg")
#
#     def __str__(self):
#         return self.meal
#
#
# class Lunch(models.Model):
#     meal = models.CharField(max_length=200)
#     calories = models.IntegerField(default=0)
#     quantity = models.IntegerField(default=0)
#     how_to_prepare = models.TextField(null=True)
#     where_to_get = models.TextField(null=True)
#     image = models.ImageField(upload_to="photos/foods", default="image/default_food.jpg")
#
#     def __str__(self):
#         return self.meal
#
#
# class Dinner(models.Model):
#     meal = models.CharField(max_length=200)
#     calories = models.IntegerField(default=0)
#     quantity = models.IntegerField(default=0)
#     how_to_prepare = models.TextField(null=True)
#     where_to_get = models.TextField(null=True)
#     image = models.ImageField(upload_to="photos/foods", default="image/default_food.jpg")
#
#     def __str__(self):
#         return self.meal
#
#
# class AWeekSchedule(models.Model):
#     week = models.IntegerField(unique=True, auto_created=True)
#     sunday_breakfast = models.ForeignKey(Breakfast, on_delete=models.CASCADE, related_name="sunday_breakfast")
#     sunday_lunch = models.ForeignKey(Lunch, on_delete=models.CASCADE, related_name="sunday_lunch")
#     sunday_dinner = models.ForeignKey(Dinner, on_delete=models.CASCADE, related_name="sunday_dinner")
#     monday_breakfast = models.ForeignKey(Breakfast, on_delete=models.CASCADE, related_name="monday_breakfast")
#     monday_lunch = models.ForeignKey(Lunch, on_delete=models.CASCADE, related_name="monday_lunch")
#     monday_dinner = models.ForeignKey(Dinner, on_delete=models.CASCADE, related_name="monday_dinner")
#     tuesday_breakfast = models.ForeignKey(Breakfast, on_delete=models.CASCADE, related_name="tuesday_breakfast")
#     tuesday_lunch = models.ForeignKey(Lunch, on_delete=models.CASCADE, related_name="tuesday_lunch")
#     tuesday_dinner = models.ForeignKey(Dinner, on_delete=models.CASCADE, related_name="tuesday_dinner")
#     wednesday_breakfast = models.ForeignKey(Breakfast, on_delete=models.CASCADE, related_name="wednesday_breakfast")
#     wednesday_lunch = models.ForeignKey(Lunch, on_delete=models.CASCADE, related_name="wednesday_lunch")
#     wednesday_dinner = models.ForeignKey(Dinner, on_delete=models.CASCADE, related_name="wednesday_dinner")
#     thursday_breakfast = models.ForeignKey(Breakfast, on_delete=models.CASCADE, related_name="thursday_breakfast")
#     thursday_lunch = models.ForeignKey(Lunch, on_delete=models.CASCADE, related_name="thursday_lunch")
#     thursday_dinner = models.ForeignKey(Dinner, on_delete=models.CASCADE, related_name="thursday_dinner")
#     friday_breakfast = models.ForeignKey(Breakfast, on_delete=models.CASCADE, related_name="friday_breakfast")
#     friday_lunch = models.ForeignKey(Lunch, on_delete=models.CASCADE, related_name="friday_lunch")
#     friday_dinner = models.ForeignKey(Dinner, on_delete=models.CASCADE, related_name="friday_dinner")
#     saturday_breakfast = models.ForeignKey(Breakfast, on_delete=models.CASCADE, related_name="saturday_breakfast")
#     saturday_lunch = models.ForeignKey(Lunch, on_delete=models.CASCADE, related_name="saturday_lunch")
#     saturday_dinner = models.ForeignKey(Dinner, on_delete=models.CASCADE, related_name="saturday_dinner")
#
#
# class ScheduleDetails(models.Model):
#     day = models.CharField(max_length=50)
#     breakfast = models.ForeignKey(Breakfast, on_delete=models.CASCADE)
#     lunch = models.ForeignKey(Lunch, on_delete=models.CASCADE)
#     dinner = models.ForeignKey(Dinner, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.day
#
#
# class Schedules(models.Model):
#     schedule_name = models.CharField(max_length=200)
#     schedule_start_date = models.DateTimeField(default=timezone.now)
#     schedule_number_of_days = models.IntegerField(default=7)
#     schedules = models.ManyToManyField(AWeekSchedule)
#
#     def __str__(self):
#         return self.schedule_name
#
#
# class MealPlan(models.Model):
#     plan_name = models.CharField(max_length=100)
#     plan_schedule = models.ManyToManyField(AWeekSchedule)
#     plan_start_date = models.DateTimeField()
#     plan_duration = models.IntegerField()
#     plan_calories_consumed = models.IntegerField()
#     plan_description = models.TextField()
#
#     def __str__(self):
#         return self.plan_name


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
    breakfast = models.TextField()

    def __str__(self):
        return self.breakfast


class LunchList(models.Model):
    class Meta:
        abstract = True
    lunch = models.TextField()

    def __str__(self):
        return self.lunch


class DinnerList(models.Model):
    class Meta:
        abstract = True
    dinner = models.TextField()

    def __str__(self):
        return self.dinner


class DayTable(BreakfastLIst, LunchList, DinnerList):
    class Meta:
        abstract = True

    day_choice = [('mon', 'monday'),
                  ('tue', 'tuesday'),
                  ('wed', 'wednesday'),
                  ('thur', 'thursday'),
                  ('fri', 'friday'),
                  ('sat', 'saturday'),
                  ('sun', 'sunday')]
    day = models.CharField(max_length=20, choices=day_choice)

    def __str__(self):
        return self.day


class PlanTable(DayTable):
    '''
    Each day meal Plan is created here.
    '''


    def __str__(self):
        return f"{self.day} - Breakfast: {self.breakfast} ..."


class MealPlansList(models.Model):
    '''
    Each of the Meal Plan is defined and created here
    The name of the plan, The content of the plan, duration and start date
    start date is null by default which gives user opportunity to start the plan anytime the user wants after enrolling.
    '''
    name = models.CharField(max_length=200)
    plan = models.ManyToManyField(PlanTable)
    duration = models.IntegerField(help_text="weeks")
    start_date = models.DateField(null=True)

    def __str__(self):
        return self.name


class MealPlans(models.Model):
    '''
    This keeps the  record of each user that has signed up for meal plan and what they signed up for.
    '''
    user = models.OneToOneField(get_user_model(), primary_key=True, on_delete=models.CASCADE)
    meal_plan = models.ForeignKey(MealPlansList, on_delete=models.CASCADE)

    def __str__(self):
        return self.meal_plan.name


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

