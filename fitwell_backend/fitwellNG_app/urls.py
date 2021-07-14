from django.urls import path
# from .views import home
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('login/', views.login_view, name='login'),
    path('sign-up/', views.sign_up, name='sign-up'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('activities/<int:pk>', views.Activities.as_view(), name='activities'),
    path('analytics/<int:pk>', views.Analytics.as_view(), name='analytics'),
    path('plans/<int:pk>', views.Plans.as_view(), name='plans'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/update/<int:pk>', views.update_user.as_view(), name='update-user'),
    # path('test/', views.TestView.as_view(), name='test'),
    path('test/<int:pk>', views.Test2View.as_view(), name='test2'),


]