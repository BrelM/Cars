from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class User(AbstractBaseUser):
    # create fields for names and login
    name = models.CharField(max_length=200, default="xx")
    login = models.CharField(unique=True, max_length=200, default="xxx")

    def __str__(self) -> str:
        return self.name
