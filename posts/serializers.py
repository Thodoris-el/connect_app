from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = Post
        fields = ('id', 'title', 'description', 'location', 'time','user','date_posted','date_updated','number_of_submits','views', 'likes')

        def create(self, validated_data):
             post = Post.objects.create(title= validated_data['title'])
             post.save()
             return post