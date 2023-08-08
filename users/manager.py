from django.contrib.auth.models import BaseUserManager


class MyUserManager(BaseUserManager):
    
   def create_user(self, email,password=None, **extra_fields):
       if not email:
           raise ValueError('Email must be provided')
       if not password:
           raise ValueError('Password must be provided')
       user = self.model(email=self.normalize_email(email), **extra_fields)
       user.set_password(password)
       user.save(using=self._db)
       return user
   
   def create_superuser(self, email,password, **kwargs):
       user = self.create_user(email,password=password, **kwargs)
       user.is_admin = True
       user.is_superuser = True
       user.save(using=self._db)
       return user