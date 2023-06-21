from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets

from .serializers import AnnouncementSerializer
from .models import *


#def AnnouncementView(viewsets.ModelViewSet):
class VisitorView(viewsets.ModelViewSet):
    serializer_class = AnnouncementSerializer
    queryset = Announcement.objects.all()
    





def index(request):
    return HttpResponse("Hello world!")

def searchCars(request, page:str):
    '''
        the page param is the name of the page
            eg: show.html
    '''
    cars = Car.object.all()
    return render(request, page, {'cars':cars})





