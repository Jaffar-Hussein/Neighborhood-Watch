from email.policy import default
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Neighbourhood(models.Model):
    name = models.CharField(max_length=50, null=False, unique=True)
    location = models.CharField(max_length=50, null=False)
    # occupants = models.IntegerField(default=0)
    admin = models.ForeignKey(User, null=False, related_name='neighbourhoods',on_delete=models.CASCADE)


class Profile(models.Model):
    user = models.OneToOneField(User, related_name="users",on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(Neighbourhood, related_name="occupants",on_delete=models.CASCADE)
