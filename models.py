from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    phone= models.CharField(max_length=100, blank=False)
  #  age = models.PositiveIntegerField(null=True, blank=True)
