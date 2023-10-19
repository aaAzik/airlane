from rest_framework import serializers
from apps.airlane.models import *
from apps.flight.models import *
from apps.plane.models import *

class AirlaneSerializers(serializers.ModelSerializer):
    class Meta:
        model = Airlane
        fields = '__all__'

class FlightSerializers(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'

class PlaneSerializers(serializers.ModelSerializer):
    class Meta:
        model = Plane   
        fields = '__all__'