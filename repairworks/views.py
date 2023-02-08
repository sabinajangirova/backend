from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from repairworks.serializer import RepairWorkSerializer

from .models import RepairWork

class RepairWorksListViewSet(ListCreateAPIView):
    serializer_class = RepairWorkSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = []

    def get_queryset(self):
        queryset = RepairWork.objects.all()
        station = self.request.query_params.get('station')
        if station is not None:
            queryset = queryset.filter(responsible__station__id=station)
        
        status = self.request.query_params.get('status')
        if status is not None:
            queryset = queryset.filter(status=status)
        return queryset

class RepairWorkViewSet(RetrieveUpdateDestroyAPIView):
    queryset = RepairWork.objects.all()
    serializer_class = RepairWorkSerializer
    serializer = RepairWorkSerializer(queryset, many=True)

    # permission_classes = [IsAuthenticated]
    permission_classes = []
    
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)