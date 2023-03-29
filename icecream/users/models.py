from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    username = models.CharField(max_length = 50, blank = True, null = True, unique = True)
    email = models.EmailField(unique=True, blank=False, null=False)
    password = models.CharField(max_length =250, blank = True, null = True)

    def __str__(self) -> str:
        return f"{self.id} {self.email}"
