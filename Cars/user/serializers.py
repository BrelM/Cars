from rest_framework import serializers
from .models import User
from visitor.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"



class CarTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarType
        fields = "__all__"


class BuilderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Builder
        fields = "__all__"


class EngineTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EngineType
        fields = "__all__"


class CarburantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carburant
        fields = "__all__"


class PowerTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PowerType
        fields = "__all__"


class SpeedTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpeedType
        fields = "__all__"




