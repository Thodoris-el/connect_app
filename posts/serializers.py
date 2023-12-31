from rest_framework import serializers
from .models import Post, Like, View, Submit


class PostSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = Post
        fields = ('id', 'title', 'description', 'location', 'time','user','date_posted','date_updated','number_of_submits','views', 'likes', 'is_active', 'key_words', 'image_url')

        def create(self, validated_data):
             post = Post.objects.create(title= validated_data['title'])
             post.save()
             return post
        
class LikeSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = Like
        fields = ('post_id', 'user_id')

    def create(self, validated_data):
        like = Like.objects.create(user_id= validated_data['user_id'], post_id= validated_data['post_id'])
        like.save()
        return like
    
class ViewSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = View
        fields = ('post_id', 'user_id')

    def create(self, validated_data):
        view = View.objects.create(user_id= validated_data['user_id'], post_id= validated_data['post_id'])
        view.save()
        return view
    
class SubmitSerializer(serializers.ModelSerializer):
    
    class Meta(object):
        model = Submit
        fields = ('post_id', 'user_id', 'is_active')

    def create(self, validated_data):
        submit = Submit.objects.create(user_id= validated_data['user_id'], post_id= validated_data['post_id'])
        submit.save()
        return submit