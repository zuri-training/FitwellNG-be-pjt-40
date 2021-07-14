from rest_framework import serializers
from fitwellNG_app.models import User, Routine, WorkoutPlanList, MealLists, MealPlans


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # this fields determines the no of fields from user model
        # that can be retirieved and save via API endpoint request
        fields = ['id','first_name', 'last_name', 'email',  'phone_no', 'height', 'weight','password']

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class RoutineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Routine
        fields = ['routine_name', 'description', 'repetition_no']


class WorkoutPlanSerializer(serializers.ModelSerializer):
    routine = RoutineSerializer(read_only=True, many=True)

    class Meta:
        model = WorkoutPlanList
        fields = ['plan', 'duration', 'daily_duration', 'routine']


class MealListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealLists
        fields = ['breakfast', 'about_breakfast', 'breakfast_calories', 'breakfast_meal_time',
                  'lunch', 'about_lunch','lunch_calories','lunch_meal_time',
                  'dinner', 'about_dinner','dinner_calories','dinner_meal_time',
                  'day', 'name', 'meal_time', 'category']


# class MealPlanListSerializer(serializers.ModelSerializer):
#     plan_table = MealPLanTableSerializer(read_only=True, many=True)
#
#     class Meta:
#         model = MealPlansList
#         fields = ['name', 'plan_table', 'duration']
#
