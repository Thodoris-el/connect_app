from django.db import models
from users.models import User
from django.utils import timezone

class Room(models.Model):
    name = models.CharField(max_length=128)


    def save(self, *args, **kwargs):
        super(Room, self).save(*args, **kwargs)
        return self 

class Message(models.Model):
    sender = models.UUIDField(null=False, blank=False)
    room = models.CharField(max_length=128)
    content = models.TextField(max_length=500)
    time_sent = models.DateTimeField(default=timezone.now(), null=False, blank=False)

    def save(self, *args, **kwargs):
        super(Message, self.save(*args, **kwargs))
        return self