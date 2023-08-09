from django.shortcuts import render
from .models import Post
from .serializers import PostSerializer
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework import status, exceptions
from django.utils import timezone
from datetime import date

# Create your views here.

class CreatePostAPIView(APIView):
    # Allow any user (authenticated or not) to access this url 
    permission_classes = (AllowAny,)
    def post(self, request):
        post = request.data
        serializer = PostSerializer(data=post)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED) 

class FinaAllView(APIView):
    permission_classes = (AllowAny,)
    def get(self, request):
        post = Post.objects.all()
        return Response(PostSerializer(post, many=True).data, status=status.HTTP_200_OK)

class FindByIdView(APIView):
    permission_classes = (AllowAny,)
    def get(self, request):
        try:
            id = request.data['id']
            post = Post.objects.all().filter(id=id).first()
            if not post:
                return exceptions.AuthenticationFailed('no post found')
            return Response(PostSerializer(post).data, status=status.HTTP_200_OK)
        except:
            raise exceptions.AuthenticationFailed('no id found')