from django.shortcuts import render
from rest_framework import generics
from fitwellNG_app.models import User
from .serializers import UserSerializer


class UserList(generics.ListAPIView):

    '''
    This API retrieve user data specified in the serializer
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreate(generics.ListCreateAPIView):
    '''
    This API creates a new user. info in serializers must be passed in
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save()
