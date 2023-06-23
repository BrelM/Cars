from rest_framework import renderers
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



class JPEGRenderer(renderers.BaseRenderer):
    media_type = 'image/jpeg'
    format = 'jpg'
    charset = None
    render_style = 'binary'

    def render(self, data, media_type=None, renderer_context=None):
        return data




