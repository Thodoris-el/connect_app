from django.shortcuts import render
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from datetime import date

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
        age_lower = date(year=today.year - request.data['ageL'], month=today.month, day=today.day)
        age_upper = date(year=today.year - request.data['ageU'], month=today.month, day=today.day)
        user = User.objects.all().filter(birthday__lt = age_lower, birthday__gt = age_upper)
        user_serializer = UserSerializer(user, many=True)
        return Response(user_serializer.data, status=status.HTTP_200_OK)
    
class SearchCustom(APIView):
    permission_classes = (AllowAny,)
    def get(self,request):
        user = User.objects.all()
        if request.data:
            data = request.data
        else:
            return Response(UserSerializer(user, many=True).data, status=status.HTTP_200_OK)
        if  'ageL' in data:
            today = timezone.now().date()
            age_lower = date(year=today.year - request.data['ageL'], month=today.month, day=today.day)
            user = user.filter(birthday__lt = age_lower)
        if 'ageU' in data:
            today = timezone.now().date()
            age_upper = date(year=today.year - request.data['ageU'], month=today.month, day=today.day)
            user = user.filter(birthday__gt = age_upper)
        if 'first_name' in data:
            user = user.filter(first_name=data['first_name'])
        if 'last_name' in data:
            user = user.filter(last_name=data['last_name'])
        if 'categories' in data:
            user = user.filter(favorites__contains=data['categories'])
        return Response(UserSerializer(user, many=True).data, status=status.HTTP_200_OK)
