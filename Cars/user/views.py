from django.shortcuts import render
from django.http import Http404, HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response

from datetime import datetime

from .serializers import *
from .models import User

from visitor.serializers import AnnouncementSerializer
from visitor.models import *

def index(request):
    return HttpResponse("Hello world!")

class UserView(APIView):
    
    # serializer_class = UserSerializer
    # queryset=User.objects.all()
    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("User Added Successfully", safe=False)
        return JsonResponse("Failled to add User", safe=False)
    
    def get_user(self, pk):
        try:
            return User.objects.get(id=pk)
        except User.DoesNotExist as e:
            raise Http404 from e
        
    def get(self, request, pk=None):
        if pk:
            data = self.get_user(pk)
            serializer = UserSerializer(data)
        else:
            data = User.objects.all()
            serializer = UserSerializer(data, many=True)
        return Response(serializer.data)
    
    def put(self, request, pk=None):
        user_to_update = User.objects.get(id=pk)
        serializer = UserSerializer(instance=user_to_update, data=request.data, partial = True)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("User Updated successfuly", safe=False)
        return JsonResponse("Failled to Update User")
    
    def delete(self, request , pk):
        user_to_delete = User.objects.get(id=pk)
        user_to_delete.delete()
        return JsonResponse("User deleted Successfully", safe=False)
    
    



class VisitorView(APIView):
    
    def get_announcement(self, pk):
        try:
            announcement = Announcement.objects.get(id=pk)
            return AnnouncementSerializer(announcement).data
        except Announcement.DoesNotExist:
            raise Http404

    def get(self, request):
        
        if request.GET.get('pk'):
            data = self.get_announcement(int(request.GET.get('pk')))
            serializer = AnnouncementSerializer(data)
        else:
            
            #data = filteringSearch(filters)
            data = Announcement.objects.filter(
                car__car_model__icontains=request.GET.get('carModel', ''),
                car__color__icontains=request.GET.get('color', ''),
                car__state__gte=int(request.GET.get('state', 0)),
                car__builder__name__icontains=request.GET.get('builder', ''),
                car__car_type__type_name__icontains=request.GET.get('type', ''),
                date__gte=datetime.strptime(request.GET.get('date', datetime.now().strftime('%d/%m/%Y')), '%d/%m/%Y'),
                price__lte=float(request.GET.get('price', 0))
                )
            if request.GET.get('orderby'):
                data = data.order_by(request.GET.get('orderby'))
            
            serializer = AnnouncementSerializer(data, many=True)
            
        return Response(serializer.data)
    
    def post(self, request):
        data = request.data
        
        # Creating an engine
        engine = Engine.objects.create(
            engine_type=EngineType.objects.get(type_name=request.data.get('engine_type', ENGINETYPE[0][1])),
            carburant=Carburant.objects.get(name=request.data.get('engine_carburant', CARBURANT[0][1])),
            power=PowerType.objects.get(type_name=request.data.get('engine_power_mode', POWERMODE[0][1])),
            speed=SpeedType.objects.get(type_name=request.data.get('engine_speed_mode', SPEED[0][1])),
            nb_horses=request.data.get('engine_nb_horses', 0)
        )
        
        # Creating a car
        car = Car.objects.create(
            car_model=request.data.get('car_model', 'Unknown model'),
            color=request.data.get('car_color', 'Unknown color'),
            state=request.data.get('car_state', 'Unknown state'),
            image=request.data.get('car_image'),
            builder=Builder.objects.get(name=request.data.get('car_builder', "Toyota")),
            car_type=CarType.objects.get(type_name=request.data.get('car_type', "Regular")),
            engine=engine,
        )
        
        #creating the announcement
        Announcement.objects.create(
            price=request.data.get('car_price', 0),
            description=request.data.get('description', "Not description provided."),
            car=car
        )
        
        return JsonResponse("Announcement Added Successfully", safe=False)
        #return JsonResponse("Failed to add announcement", safe=False)

    def put(self, request):
        pass
    
    
    
    
class CarTypeView(APIView):
    
    def get(self, request):
        data = CarType.objects.all()
        serializer = CarTypeSerializer(data, many=True)
        return Response(serializer.data)


class BuilderView(APIView):
    
    def get(self, request):
        data = Builder.objects.all()
        serializer = BuilderSerializer(data, many=True)
        return Response(serializer.data)


class EngineTypeView(APIView):
    
    def get(self, request):
        data = EngineType.objects.all()
        serializer = EngineTypeSerializer(data, many=True)
        return Response(serializer.data)

class CarburantView(APIView):
    
    def get(self, request):
        data = Carburant.objects.all()
        serializer = CarburantSerializer(data, many=True)
        return Response(serializer.data)

class PowerTypeView(APIView):
    
    def get(self, request):
        data = PowerType.objects.all()
        serializer = PowerTypeSerializer(data, many=True)
        return Response(serializer.data)


class SpeedTypeView(APIView):
    
    def get(self, request):
        data = SpeedType.objects.all()
        serializer = SpeedTypeSerializer(data, many=True)
        return Response(serializer.data)



