from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import UserManager

class User(AbstractUser):
    nick_name = models.CharField(max_length=120, unique=True)
    email = models.EmailField(unique=True, max_length=80)
    token = models.CharField(max_length=15, unique=True)
    username = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["nick_name"]

    objects = UserManager()

    def __str__(self):
        return self.email

