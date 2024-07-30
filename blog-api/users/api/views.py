
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from rest_framework import status

from ..models import CustomUser
from .serializers import CustomUserSerializer, CustomUserInfoSerializer

@api_view(['POST'])
def register(request):
    serializer = CustomUserSerializer(data=request.data)

    if serializer.is_valid():
        user = CustomUser.objects.create_user(
            email = serializer.validated_data['email'],
            password = serializer.validated_data['password'],
            nickname = serializer.validated_data['nickname'],
            first_name = serializer.validated_data['first_name'],
            last_name = serializer.validated_data['last_name'],
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_users(request):

    if request.method == 'GET':
        users = CustomUser.objects.filter(is_active = True)

        serializer = CustomUserInfoSerializer(users, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
        

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_info(request):

    if request.method == 'GET':

        user = request.user
        model = CustomUser.objects.get(id=user.id)
        
        serializer = CustomUserInfoSerializer(model)

        return Response(serializer.data, status=status.HTTP_200_OK)

