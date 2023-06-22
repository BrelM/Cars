from rest_framework import serializers
from .models import User
from visitor.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'login', 'password')



class CarTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarType
        fields = ('type_name', 'nb_seats')


class BuilderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Builder
        fields = ('name', 'hq')


class EngineTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EngineType
        fields = ('type_name')


class CarburantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carburant
        fields = ('name')


class PowerTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PowerType
        fields = ('type_name')


class SpeedTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpeedType
        fields = ('type_name')




