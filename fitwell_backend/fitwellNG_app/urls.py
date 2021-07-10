from django.urls import path
# from .views import home
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('login/', views.login_view, name='login'),
    path('sign-up/', views.sign_up, name='sign-up'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('plans/', views.Plans.as_view(), name='plans'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/update/<int:pk>', views.update_user.as_view(), name='update-user')

]