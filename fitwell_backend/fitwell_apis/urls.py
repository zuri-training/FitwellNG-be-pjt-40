from django.urls import path
from .views import UserCreate, UserList, RoutineList, RoutineCreate, WorkoutPlanLists,\
    WorkoutPlanCreate, MealTableList, MealTableCreate, MealPlanList, MealPlanCreate
from rest_framework.authtoken import views

urlpatterns = [
    path('api/users/', UserList.as_view(), name='user_list'),   # GET displaying all users
    path('api/users/create/', UserCreate.as_view(), name='user_create'),     # creating a new user
    path('api/users/get-token/', views.obtain_auth_token, name='api-token-auth'),  # POST getting a token to be used for performing CRUD

    path('api/services/routines/', RoutineList.as_view(), name='routine-list'),
    path('api/services/routines/create/', RoutineCreate.as_view(), name='routine-create'),

    path('api/services/workoutplan/', WorkoutPlanLists.as_view(), name='workout-plan-list'),
    path('api/services/workoutplan/create/', WorkoutPlanCreate.as_view(), name='workout-plan-create'),

    path('api/services/mealtable/', MealTableList.as_view(), name='meal-table-list'),
    path('api/services/mealtable/create/', MealTableCreate.as_view(), name='meal-table-create'),

    path('api/services/mealplan/', MealPlanList.as_view(), name='meal-plan-list'),
    path('api/services/mealplan/create/', MealPlanCreate.as_view(), name='meal-plan-create'),

]