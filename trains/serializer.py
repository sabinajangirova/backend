from .models import Train
from rest_framework.serializers import ModelSerializer


class TrainSerializer(ModelSerializer):
    class Meta:
        model = Train
        fields = ['id', 'name', 'longitude', 'latitude', 'conductor', 'departureStation', 'destinationStation']