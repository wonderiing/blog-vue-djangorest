
from rest_framework import serializers
from ..models import CustomUser
from blog.api.serializers import UserPostSerializer

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class CustomUserInfoSerializer(serializers.ModelSerializer):

    user_post = UserPostSerializer(many=True, read_only = True)

    class Meta:
        model = CustomUser
        exclude = ('is_active', 'password','is_staff', 'last_login', 'is_superuser', 'user_permissions', 'groups')