from django.shortcuts import render
from django.http import HttpResponse

from .models import Cars


def index(request):
    return HttpResponse("Hello world!")

def searchCars(request, page:str):
    '''
        the page param is the name of the page
            eg: show.html
    '''
    cars = Cars.object.all()
    return render(request, page, {'cars':cars})

# def searchACar