from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import UserSerializer
from .models import User

def index(request):
    return HttpResponse("Hello wolrd!")

class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset=User.objects.all()
