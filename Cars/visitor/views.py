from django.http.response import Http404
from django.db import models
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets

from datetime import datetime

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
    def get(self, request):
        #data = filteringSearch(filters)
        data = Announcement.objects.filter(
            model__icontains=request.GET.get('carModel', ''),
            color__icontains=request.GET.get('color', ''),
            state__gte=int(request.GET.get('state', 0)),
            builder__name__icontains=request.GET.get('builder', ''),
            car_type__type_name__icontains=request.GET.get('type', ''),
            date__lte=datetime.strptime(request.GET.get('date', datetime.now().strftime('%d/%m/%Y')), '%d/%m/%Y'),
            price__lte=float(request.GET.get('price', 1e120))
            )
        
        if request.GET.get('orderby'):
            data = data.order_by(request.GET.get('orderby'))
        
        serializer = AnnouncementSerializer(data, many=True)
        
        return Response(serializer.data)



@csrf_exempt
def login(request):
    if request.method == 'POST':
        user_data = request.POST
        user = User.objects.get(login=user_data.get('login'), password=user_data.get('password'))
        
        if user:
            request.session['user_id'] = user.id
            request.session['user_login'] = user.login
            request.session['user_name'] = user.name
            
            return JsonResponse(UserSerializer(user).data)
        return JsonResponse('Account not found.')
    return JsonResponse('Bad request.')
    



