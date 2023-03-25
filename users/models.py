from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    username = models.CharField(max_length = 50, blank = True, null = True, unique = True)
    email = models.EmailField(unique=True, blank=False, null=False)
    native_name = models.CharField(max_length = 5)
    phone_no = models.CharField(max_length = 10)