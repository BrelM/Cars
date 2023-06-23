from rest_framework import serializers
from .models import *

class AnnouncementSerializer(serializers.ModelSerializer):
    #car_image = serializers.ImageField(source='image')
    builder_name = serializers.CharField(source='builder.name')
    car_type_name = serializers.CharField(source='car_type.type_name')
    engine_type_name = serializers.CharField(source='engine_type.type_name')
    carburant_type = serializers.CharField(source='carburant.name')
    power_type = serializers.CharField(source='power.type_name')
    speed_type = serializers.CharField(source='speed.type_name')
    
    
    class Meta:
        model = Announcement
        fields = ('id', 'date', 'price', 'description', 'model', 'color', 'image', 'state', 'builder_name', 'car_type_name', 'engine_type_name', 'carburant_type', 'power_type', 'speed_type', 'nb_horses')

    '''   
    def get_car(self, obj):
        return obj.get_image_url()
    '''



