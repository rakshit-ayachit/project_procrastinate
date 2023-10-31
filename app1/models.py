# Create your models here.

from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    additional_info = models.TextField(blank=True, null=True)
