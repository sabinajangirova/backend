from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from trainstations.serializer import TrainStationSerializer

from .models import TrainStation

class TrainStationViewSet(ModelViewSet):
    queryset = TrainStation.objects.all()
    serializer_class = TrainStationSerializer
    serializer = TrainStationSerializer(queryset, many=True)
    permission_classes = [IsAuthenticated]
    # permission_classes = []

