from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin)
# Create your models here.

class User(AbstractBaseUser , PermissionsMixin):
    email = models.EmailField(max_length = 255 , unique=True)
    is_staff = models.BooleanField(default = False)
    is_active = models.BooleanField(default=True)
    # is_verified = models.CharField(default = False)
    first_name = models.CharField(max_length=20)
    REQUIRED_FIELDS = []

    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.email
