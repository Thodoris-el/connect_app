from django.db import models
from users.models import User
from django.utils import timezone
import uuid

# Create your models here.
class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=80, null=False, blank=False)
    description = models.TextField(max_length=1000, blank=True, null=True)
    location = models.TextField(max_length=100, blank=True, null=True)
    time = models.DateTimeField(max_length=100, blank=True, null=True)
    user = models.UUIDField(null=False, blank=False)
    date_posted = models.DateTimeField(default=timezone.now(), null=False, blank=False)
    date_updated = models.DateTimeField(default=timezone.now(), null=False, blank=False)
    number_of_submits = models.IntegerField(default=0, blank=False, null=False)
    views = models.IntegerField(default=0, blank=False, null=False)
    likes = models.IntegerField(default=0, blank=False, null=False)

    def save(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs)
        return self