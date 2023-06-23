from django.db import models
# from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class User(models.Model):
    # create fields for names and login
    login = models.EmailField(unique=True, max_length=200, default="xxx", primary_key=True)
    name = models.CharField(max_length=200, default="xx")
    password = models.CharField(max_length=200, default="")

    def __str__(self) -> str:
        return f"User name : {self.name}"