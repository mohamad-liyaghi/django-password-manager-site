from django.contrib.auth.models import BaseUserManager
import random

class UserManager(BaseUserManager):
    def create_user(self, nick_name, email, password, **extra_fields):
        if not nick_name:
            raise ValueError("Users must have nick name")

        if not email:
            raise ValueError("Users must have email")

        email = self.normalize_email(email)
        token = random.randint(1, 99999999999999)

        user = self.model(nick_name= nick_name, email= email, token= token, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, nick_name, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(nick_name= nick_name, email= email, password= password, **extra_fields)