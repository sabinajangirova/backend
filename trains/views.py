from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from trains.serializer import TrainSerializer

from .models import Train

class TrainViewSet(ModelViewSet):
    queryset = Train.objects.all()
    serializer_class = TrainSerializer
    serializer = TrainSerializer(queryset, many=True)
    # permission_classes = [IsAuthenticated]