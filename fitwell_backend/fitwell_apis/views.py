from django.shortcuts import render
from rest_framework import generics
from fitwellNG_app.models import User, Routine, WorkoutPlanList, PlanTable, MealPlansList
from .serializers import UserSerializer, RoutineSerializer, WorkoutPlanSerializer, MealPLanTableSerializer, MealPlanListSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class UserList(generics.ListAPIView):
    '''
    This API retrieve user data specified in the serializer
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class UserCreate(generics.ListCreateAPIView):
    '''
    This API creates a new user. info in serializers must be passed in
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save()


class RoutineList(generics.ListAPIView):
    queryset = Routine.objects.all()
    serializer_class = RoutineSerializer


class RoutineCreate(generics.ListCreateAPIView):
    queryset = Routine.objects.all()
    serializer_class = RoutineSerializer

    def perform_create(self, serializer):
        serializer.save()


class WorkoutPlanLists(generics.ListAPIView):
    queryset = WorkoutPlanList.objects.all()
    serializer_class = WorkoutPlanSerializer


class WorkoutPlanCreate(generics.ListCreateAPIView):
    queryset = WorkoutPlanList.objects.all()
    serializer_class = WorkoutPlanSerializer

    def perform_create(self, serializer):
        serializer.save()


class MealTableList(generics.ListAPIView):
    queryset = MealPlansList.objects.all()
    serializer_class = MealPLanTableSerializer


class MealTableCreate(generics.ListCreateAPIView):
    queryset = MealPlansList.objects.all()
    serializer_class = MealPLanTableSerializer

    def perform_create(self, serializer):
        serializer.save()


class MealPlanList(generics.ListAPIView):
    queryset = MealPlansList.objects.all()
    serializer_class = MealPlanListSerializer


class MealPlanCreate(generics.ListCreateAPIView):
    queryset = MealPlansList.objects.all()
    serializer_class = MealPlanListSerializer

    def perform_create(self, serializer):
        serializer.save()
