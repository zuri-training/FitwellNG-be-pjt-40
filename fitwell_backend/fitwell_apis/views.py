from django.shortcuts import render
from rest_framework import generics
from fitwellNG_app.models import User
from .serializers import UserSerializer
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
