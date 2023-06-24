from django.shortcuts import render

from django.http import Http404, HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework import viewsets
from rest_framework.response import Response

from datetime import datetime
import pickle

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
        try:
            user = User.objects.get(login=data.get('login'))
            if user:
                return JsonResponse({'error' : 'Login already taken.'}, safe=False)
            
        except User.DoesNotExist:
            pass
        
                        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"user":serializer}, safe=False)
        return JsonResponse({'error' : "Failled to add User"}, safe=False)
    
    def get_user(self, login):
        try:
            return User.objects.get(login=login)
        except User.DoesNotExist as e:
            raise Http404 from e
        
    def get(self, request, login=None):
        if login:
            data = self.get_user(login)
            serializer = UserSerializer(data)
        else:
            data = User.objects.all()
            serializer = UserSerializer(data, many=True)
        return Response(serializer.data)
    
    
    def put(self, request, login=None):
        user_to_update = User.objects.get(login=login)
        serializer = UserSerializer(instance=user_to_update, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("User Updated successfuly", safe=False)
        return JsonResponse({'error' : "Failled to Update User"})
    
    def delete(self, request, login):
        user_to_delete = User.objects.get(login=login)
        user_to_delete.delete()
        return JsonResponse("User deleted Successfully", safe=False)
    
    



class UserAnnouncementView(APIView):
    
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
                model__icontains=request.GET.get('carModel', ''),
                color__icontains=request.GET.get('color', ''),
                state__gte=int(request.GET.get('state', 0)),
                builder__name__icontains=request.GET.get('builder', ''),
                car_type__type_name__icontains=request.GET.get('type', ''),
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
        try:
            with open("user_info.info", "rb") as info:
                session = pickle.Unpickler(info).load()

                announcement = Announcement.objects.create(
                    user=User.objects.get(login=session.get('user_login', "")),
                    engine_type=EngineType.objects.get(type_name=request.data.get('engine_type', ENGINETYPE[0][1])),
                    carburant=Carburant.objects.get(name=request.data.get('engine_carburant', CARBURANT[0][1])),
                    power=PowerType.objects.get(type_name=request.data.get('engine_power_mode', POWERMODE[0][1])),
                    speed=SpeedType.objects.get(type_name=request.data.get('engine_speed_mode', SPEED[0][1])),
                    nb_horses=request.data.get('engine_nb_horses', 0),
                    model=request.data.get('car_model', 'Unknown model'),
                    color=request.data.get('car_color', 'Unknown color'),
                    state=request.data.get('car_state', 0),
                    image=request.data.get('car_image'),
                    builder=Builder.objects.get(name=request.data.get('car_builder', "Toyota")),
                    car_type=CarType.objects.get(type_name=request.data.get('car_type', "Regular")),
                    price=request.data.get('car_price', 0),
                    description=request.data.get('description', "Not description provided."),
                )
                return JsonResponse("Announcement Added Successfully", safe=False)
        except:
            return JsonResponse({'error' : "Failed to add announcement"}, safe=False)

    def put(self, request, id):
        to_update = Announcement.objects.get(id=id)

        #try:
        to_update.engine_type=EngineType.objects.get(type_name=request.data.get('engine_type', to_update.engine_type.type_name))
        to_update.carburant=Carburant.objects.get(name=request.data.get('engine_carburant', to_update.carburant.name))
        to_update.power=PowerType.objects.get(type_name=request.data.get('engine_power_mode', to_update.power.type_name))
        to_update.speed=SpeedType.objects.get(type_name=request.data.get('engine_speed_mode', to_update.speed.type_name))
        to_update.nb_horses=request.data.get('engine_nb_horses', to_update.nb_horses)
        to_update.model=request.data.get('car_model', to_update.model)
        to_update.color=request.data.get('car_color', to_update.color)
        to_update.state=request.data.get('car_state', to_update.state)
        to_update.image=request.data.get('car_image', to_update.image)
        to_update.builder=Builder.objects.get(name=request.data.get('car_builder', to_update.builder.name))
        to_update.car_type=CarType.objects.get(type_name=request.data.get('car_type', to_update.car_type.type_name))
        to_update.price=request.data.get('car_price', to_update.price)
        to_update.description=request.data.get('description', to_update.description)        

        to_update.save()
        return JsonResponse("Annnouncement Updated successfuly.", safe=False)
        #except:
        #return JsonResponse({'error' : "Failled to Update Annnouncement."})
    
    def delete(self, request, id):
        to_delete = Announcement.objects.get(id=id)
        to_delete.delete()
        return JsonResponse("Announcement deleted Successfully", safe=False)




class MyAnnouncementView(APIView):
    
    def get(self, request):
        with open("user_info.info", "rb") as info:
            session = pickle.Unpickler(info).load()
        
            data = Announcement.objects.filter(user__login=session['user_login'])
            serializer = AnnouncementSerializer(data, many=True)
            return Response(serializer.data)
    
    
    
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



def logout(request):
    with open("user_info.info", "wb") as info:
        pass
    
    return JsonResponse({"message" : "You're currently logged out."}, safe=False)
