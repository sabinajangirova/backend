from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from repairworks.serializer import RepairWorkSerializer

from .models import RepairWork

class RepairWorkViewSet(ModelViewSet):
    queryset = RepairWork.objects.all()
    serializer_class = RepairWorkSerializer
    serializer = RepairWorkSerializer(queryset, many=True)
    permission_classes = [IsAuthenticated]