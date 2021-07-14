from django.shortcuts import render
from rest_framework import generics
from fitwellNG_app.models import User, Routine, WorkoutPlanList, MealPlans, MealLists
from .serializers import UserSerializer, RoutineSerializer, WorkoutPlanSerializer, MealListSerializer
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
    permission_classes = [IsAdminUser, IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class RoutineList(generics.ListAPIView):
    queryset = Routine.objects.all()
    serializer_class = RoutineSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]


class RoutineCreate(generics.ListCreateAPIView):
    queryset = Routine.objects.all()
    serializer_class = RoutineSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class WorkoutPlanLists(generics.ListAPIView):
    queryset = WorkoutPlanList.objects.all()
    serializer_class = WorkoutPlanSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]


class WorkoutPlanCreate(generics.ListCreateAPIView):
    queryset = WorkoutPlanList.objects.all()
    serializer_class = WorkoutPlanSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class MealListView(generics.ListAPIView):
    queryset = MealLists.objects.all()
    serializer_class = MealListSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]


class MealCreateView(generics.ListCreateAPIView):
    queryset = MealLists.objects.all()
    serializer_class = MealListSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


# class MealPlanList(generics.ListAPIView):
#     queryset = MealPlansList.objects.all()
#     serializer_class = MealPlanListSerializer
#     permission_classes = [IsAdminUser, IsAuthenticated]
#
#
# class MealPlanCreate(generics.ListCreateAPIView):
#     queryset = MealPlansList.objects.all()
#     serializer_class = MealPlanListSerializer
#     permission_classes = [IsAdminUser, IsAuthenticated]
#
#     def perform_create(self, serializer):
#         serializer.save()
