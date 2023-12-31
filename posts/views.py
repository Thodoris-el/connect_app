from django.shortcuts import render
from .models import Post, Like, View, Submit
from .serializers import PostSerializer, LikeSerializer, ViewSerializer, SubmitSerializer
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
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

class FindAllView(APIView):
    permission_classes = (AllowAny,)
    def get(self, request):
        post = Post.objects.all()
        return Response(PostSerializer(post, many=True).data, status=status.HTTP_200_OK)

class FindByIdView(APIView):
    permission_classes = (AllowAny,)
    def get(self, request):
        try:
            post_id = request.data['post_id']
            user_id = request.data['user_id']
        except:
            raise exceptions.AuthenticationFailed('no id found')
        post = Post.objects.all().filter(id=post_id).first()
        if not post:
            return Response({'no post found'}, status=status.HTTP_404_NOT_FOUND)
        view = View.objects.all().filter(post_id=post_id, user_id=user_id)
        if not view:
            post.views += 1
            post.save()
            view = ViewSerializer(data={'post_id': post_id, 'user_id': user_id})
            view.is_valid()
            view.save()
        return Response(PostSerializer(post).data, status=status.HTTP_200_OK)

class FindByUserView(APIView):
    permission_classes = (AllowAny,)
    def get(self, request):
        try:
            id = request.data['user']
        except:
            raise exceptions.AuthenticationFailed('no id found')
        post = Post.objects.all().filter(user=id)
        if not post:
            return Response({'no post found'}, status=status.HTTP_404_NOT_FOUND)
        return Response(PostSerializer(post, many=True).data, status=status.HTTP_200_OK)

class FindByDateView(APIView):
    permission_classes = (AllowAny,)
    def get(self, request):
        try:
            date = request.data['date']
        except:
            raise exceptions.AuthenticationFailed('no id found')
        post = Post.objects.all().filter(time=date)
        if not post:
            return Response({'no post found'}, status=status.HTTP_404_NOT_FOUND)
        return Response(PostSerializer(post, many=True).data, status=status.HTTP_200_OK)
       
class FindByLocationView(APIView):
    permission_classes = (AllowAny,)
    def get(self, request):
        try:
            location = request.data['location']
        except:
            raise exceptions.AuthenticationFailed('no location found')
        post = Post.objects.all().filter(location=location)
        if not post:
            return Response({'no post found'}, status=status.HTTP_404_NOT_FOUND)
        return Response(PostSerializer(post, many=True).data, status=status.HTTP_200_OK)

class LikePostView(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        try:
            post_id = request.data['post_id']
            user_id = request.data['user_id']
        except:
            raise exceptions.AuthenticationFailed('no id found')
        
        like = Like.objects.all().filter(post_id=post_id, user_id=user_id)
        if like:
            return Response({'already liked'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        post = Post.objects.all().filter(id=post_id).first()
        if not post:
            return Response({'no post found'}, status=status.HTTP_404_NOT_FOUND)
        post.likes += 1
        post.save()
        like = LikeSerializer(data={'post_id': post_id, 'user_id': user_id})
        like.is_valid()
        like.save()
        return Response(PostSerializer(post).data, status=status.HTTP_200_OK)
        
class DislikePostView(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        try:
            post_id = request.data['post_id']
            user_id = request.data['user_id']
        except:
            raise exceptions.AuthenticationFailed('no id found')
        like = Like.objects.all().filter(post_id=post_id, user_id=user_id)
        if not like:
            return Response({'not liked to dislike'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        post = Post.objects.all().filter(id=post_id).first()
        if not post:
            return Response({'no post found'}, status=status.HTTP_404_NOT_FOUND)
        if post.likes != 0:
            post.likes -= 1
        post.save()
        like.delete()
        return Response(PostSerializer(post).data, status=status.HTTP_200_OK)
    
class Top100View(APIView):
    permission_classes = (AllowAny,)
    def get(self, request):
        posts = Post.objects.all().order_by('-likes')[:100]
        if not posts:
            return Response({'no posts found'}, status=status.HTTP_404_NOT_FOUND)
        return Response(PostSerializer(posts, many=True).data, status=status.HTTP_200_OK)

class FindPostCustom(APIView):
    permission_classes = (AllowAny,)
    def get(self,request):
        posts = Post.objects.all()

        if 'start_date' in request.data:
            posts = posts.filter(time__gt=request.data['start_date'])
        if 'end_date' in request.data:
            posts = posts.filter(time__lt=request.data['end_date'])
        if 'location' in request.data:
            posts = posts.filter(location=request.data['location'])
        if 'keywords' in request.data:
            posts = posts.filter(keywords=request.data['keywords'])
        return Response(PostSerializer(posts,many=True).data, status=status.HTTP_200_OK)

class SubmitView(APIView):
    permission_classes = (AllowAny,)
    def post(self,request):
        try:
            post_id = request.data['post_id']
            user_id = request.data['user_id']
        except:
            raise exceptions.AuthenticationFailed('no id found')
        post = Post.objects.all().filter(id=post_id).first()
        if not post:
            return Response({'no post found'}, status=status.HTTP_404_NOT_FOUND)
        if str(post.user) == user_id:
            return Response({"can't submit on your own post"}, status=status.HTTP_400_BAD_REQUEST)
        submit =  Submit.objects.all().filter(post_id=post_id, user_id=user_id).first()
        if submit:
            if submit.is_active == False:
                submit.is_active = True
                submit.save()
                post.number_of_submits += 1
                post.save()
                return Response(PostSerializer(post).data, status=status.HTTP_200_OK)
            else:
                return Response({"already submitted"}, status=status.HTTP_208_ALREADY_REPORTED)
        else:
            submit = SubmitSerializer(data={'post_id': post_id, 'user_id': user_id})
            submit.is_valid()
            submit.save()
            post.number_of_submits += 1
            post.save()
            return Response(PostSerializer(post).data, status=status.HTTP_200_OK)

class CancelSubmit(APIView):
    permission_classes = (AllowAny,)
    def post(self,request):
        try:
            post_id = request.data['post_id']
            user_id = request.data['user_id']
        except:
            raise exceptions.AuthenticationFailed('no id found')
        post = Post.objects.all().filter(id=post_id).first()
        if not post:
            return Response({'no post found'}, status=status.HTTP_404_NOT_FOUND)
        if str(post.user) == user_id:
            return Response({"can't submit on your own post"}, status=status.HTTP_400_BAD_REQUEST)
        submit =  Submit.objects.all().filter(post_id=post_id, user_id=user_id).first()
        if not submit:
            return Response({"haven't submitted to cancel submit"})
        if submit.is_active:
            submit.is_active = False
            submit.save()
            post.number_of_submits -= 1
            post.save()
            return Response({" submit canceled"}, status=status.HTTP_200_OK)
        else:
            return Response({"already canceled submit"}, status=status.HTTP_208_ALREADY_REPORTED)