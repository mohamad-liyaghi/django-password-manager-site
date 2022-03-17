from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class passwordModel(models.Model):
    title = models.CharField(max_length=120)
    password = models.CharField(max_length=120)
    owner = models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE)
    def __str__(self):
        return  self.title