from rest_framework import serializers
from .models import Room, Message


class RoomSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = Room
        fields = ('name')

        def create(self, validated_data):
             room = Room.objects.create(name= validated_data['name'])
             room.save()
             return room
        
class MessageSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = Message
        fields = ('sender', 'room', 'content', 'time_sent')

    def create(self, validated_data):
        message = Message.objects.create(sender= validated_data['sender'], room= validated_data['room'])
        message.save()
        return message
