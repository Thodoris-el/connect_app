from django.shortcuts import render
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone

# Create your views here.
User = get_user_model()

class CreateUserAPIView(APIView):
    # Allow any user (authenticated or not) to access this url 
    permission_classes = (AllowAny,)
    def post(self, request):
        request.data['password'] = make_password(request.data['password'])
        user = request.data
        serializer = UserSerializer(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)  

class GetAllUser(APIView):
    permission_classes = (AllowAny,)
    def get(self,request):
        users = User.objects.all()
        users_serializer = UserSerializer(users, many =True)
        return Response(users_serializer.data, status=status.HTTP_200_OK)
    
class SearchUserByName(APIView):
    permission_classes = (AllowAny,)
    def get(self,request):
        name = request.data['first_name']
        user = User.objects.filter(first_name=name).values()
        user_serializer = UserSerializer(user, many=True)
        return Response(user_serializer.data, status=status.HTTP_200_OK)
    
class SearchUserByAge(APIView):
    permission_classes = (AllowAny,)
    def get(self,request):
        today = timezone.now().date()
        age_lower = today 
        age_lower.year = today.year - request.data['ageL']
        age_upper = today
        age_upper.year = today.year - request.data['ageU']
        user = User.objects.all().filter(birthday__gt = age_lower, birthday__lt = age_upper)
        user_serializer = UserSerializer(user, many=True)
        return Response(user_serializer.data, status=status.HTTP_200_OK)
