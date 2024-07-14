from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from uuid import uuid4
from random import randint
from user.manager import UserManager

class User(AbstractBaseUser,PermissionsMixin) :
    id = models.UUIDField(default=uuid4(),primary_key=True)
    email = models.EmailField(unique=True)
    username = models.SlugField(unique=True)
    joind = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    otp = models.SlugField(null=True,blank=True,max_length=6)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = UserManager()

    def __str__(self) : 
        return self.email
    
    def save(self,**kwargs) : 
        self.otp = randint(100000,999999)
        return super().save(**kwargs)