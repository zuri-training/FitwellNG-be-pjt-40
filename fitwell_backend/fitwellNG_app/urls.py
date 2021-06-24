from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('', include('django.contrib.auth.urls')),
    path('sign-up/', views.sign_up, name='sign-up'),
    path('', views.home, name='home'),
]