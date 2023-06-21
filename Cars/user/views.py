from django.shortcuts import render
from django.http import Http404, HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import User

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