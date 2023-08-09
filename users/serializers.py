from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):

    creation_date = serializers.ReadOnlyField()

    class Meta(object):
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'is_active','is_admin','is_premium','creation_date','update_date','last_request', 'password', 'birthday', 'description', 'favorites')

        def create(self, validated_data):
             user = User.objects.create(email= validated_data['email'])
             user.set_password(validated_data['password'])
             user.save()
             return user
        