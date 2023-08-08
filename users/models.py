from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import MyUserManager
from django.utils import timezone
import uuid

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=40,null=False, blank=False)
    last_name = models.CharField(max_length=40,null=False, blank=False)
    birthday = models.DateField(null=False, blank=False)
    description = models.TextField(max_length=1000, blank=True, null=True)
    favorites = models.JSONField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_premium = models.BooleanField(default=False)
    creation_date = models.DateTimeField(default=timezone.now())
    update_date = models.DateTimeField(default=timezone.now())
    last_request = models.DateTimeField(default=timezone.now())

    objects = MyUserManager() 

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
    
    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        return self