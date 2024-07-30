
from django.contrib import admin
from django.urls import path

from .views import register, get_users, get_user_info

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', register, name ='register'),
    path('users/', get_users, name='get-users'),
    path('usersinfo/', get_user_info, name='get-users-info')

]


