from asyncio.windows_events import NULL
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True)
    isPremium = models.BooleanField(default=False,blank=True)
    subTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.subTime)


class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=60, default=NULL, null=True, blank=True )
    name = models.CharField(max_length=200, null=True, blank=True)
    content = models.CharField(max_length=700, default=NULL)
    createdAt = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return str(self.createdAt)