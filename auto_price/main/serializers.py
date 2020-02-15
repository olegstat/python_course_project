from rest_framework import serializers
from .models import CarBase

class CarBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBase
        fields=('make', 'model')