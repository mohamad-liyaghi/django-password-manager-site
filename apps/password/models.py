from django.db import models
from accounts.models import User


class Password(models.Model):
    title = models.CharField(max_length=120)
    password = models.CharField(max_length=120)
    owner = models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE, related_name="password_owner")
    token = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return  self.title