from django.urls import path
from .views import UserCreate, UserList
from rest_framework.authtoken import views

urlpatterns = [
    path('api/users/', UserList.as_view(), name='user_list'),   # displaying all users
    path('api/users/create/', UserCreate.as_view(), name='user_create'),     # creating a new user
    path('api/users/get-token/', views.obtain_auth_token, name='api-token-auth')  # getting a token to be used for performing CRUD
]