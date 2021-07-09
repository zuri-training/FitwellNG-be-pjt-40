from rest_framework import serializers
from fitwellNG_app.models import User, Routine, WorkoutPlanList, PlanTable, MealPlansList


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
        fields = ['plan', 'duration', 'routine']


class MealPLanTableSerializer(serializers.ModelSerializer):
    class Meta:
        model =PlanTable
        fields =['breakfast', 'lunch', 'dinner', 'day']


class MealPlanListSerializer(serializers.ModelSerializer):
    plan_table = MealPLanTableSerializer(read_only=True, many=True)

    class Meta:
        model = MealPlansList
        fields = ['name', 'plan_table', 'duration']

