from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    is_BrgyStaff = models.BooleanField(default=False)
    is_Constituent = models.BooleanField(default=False)

class BrgyStaff(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username

class Constituent(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255,blank=True)
    Address = models.CharField(max_length=255)
    def __str__(self):
        return self.user.username
