from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings


class UserAccountManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, username, password= None):
        if not email:
            raise ValueError('Please enter a valid email address')
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            first_name = first_name,
            last_name = last_name,
            username=username,
        )
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,first_name, last_name, email, username, password=None):
        user = self.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password
        )
        user.is_admin = True
        user.is_staff =True
        user.is_superuser = True
        user.save()
        return user

class UserAccount(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    username = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    
    objects = UserAccountManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    
