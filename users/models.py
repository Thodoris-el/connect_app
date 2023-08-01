from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
import datetime
import uuid

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=40,null=False, blank=False)
    birthday = models.DateField(null=False, blank=False)
    age = models.PositiveIntegerField(null=False, blank=False)
    description = models.TextField(max_length=1000, blank=True, null=True)
    favorites = models.JSONField(blank=True, null=True)