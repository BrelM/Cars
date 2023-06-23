from django.http.response import Http404
from django.db import models
from django.db.models import F, Q

from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets

from datetime import datetime
import pickle
import json

from .serializers import AnnouncementSerializer
from .models import *

from user.serializers import UserSerializer



#def AnnouncementView(viewsets.ModelViewSet):
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
            data = Announcement.objects.all()
            serializer = AnnouncementSerializer(data, many=True)
            
        return Response(serializer.data)


class VisitorSearchView(APIView):
    def post(self, request):
        filters = json.loads(request.body)
        
        data = Announcement.objects.filter(
            Q(model__icontains=filters.get('carModel', '')) | Q(model__contains=filters.get('keyword', '')),
            Q(builder__name__icontains=filters.get('builder', '')) | Q(builder__name__icontains=filters.get('keyword', '')),
            Q(color__icontains=filters.get('color', '')) | Q(color__icontains=filters.get('keyword', '')),
            state__gte=int(filters.get('state', 0)),
            car_type__type_name__icontains=filters.get('type', ''),
            power__type_name__icontains=filters.get('power', ''),
            speed__type_name__icontains=filters.get('speed', ''),
            carburant__type_name__icontains=filters.get('carburant', ''),
            date__gte=datetime.strptime(filters.get('date', datetime.now().strftime('%d/%m/%Y')), '%d/%m/%Y'),
            price__lte=float(filters.get('price', 1e120))
        )
        
        if request.GET.get('orderby'):
            data = data.order_by(request.GET.get('orderby'))
        
        serializer = AnnouncementSerializer(data, many=True)
        
        return Response(serializer.data)



@csrf_exempt
def login(request):
    if request.method == 'POST':
        user_data = json.loads(request.body)
        try:
            user = User.objects.get(login=user_data.get('login'), password=user_data.get('password'))
        except User.DoesNotExist:
            return JsonResponse('Account not found.', safe=False)
        
        session = {'user_login' : user.login, 'user_password': user.password}
        with open("user_info.info", "wb") as info:
            pickle.Pickler(info).dump(session)

        return JsonResponse(UserSerializer(user).data)
    return JsonResponse('Bad request.', safe=False)



