from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from users.permissions import isStationWorker
from repairworks.serializer import RepairWorkSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import RepairWork
import json

class RepairWorksListViewSet(ListCreateAPIView):
    serializer_class = RepairWorkSerializer
    permission_classes = [IsAuthenticated, isStationWorker]

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

    permission_classes = [IsAuthenticated, isStationWorker]
    
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class RepairWorkCreateListViewSet(CreateAPIView):
    serializer_class = RepairWorkSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        repairworks = request.data["repairworks"]
        new_repairworks = []
        not_created_repairworks = []
        for r in repairworks:
            serializer = RepairWorkSerializer(data=r)
            if not serializer.is_valid():
                not_created_repairworks.append(r)
            repairwork = serializer.create(serializer.validated_data)
            new_repairworks.append(json.dumps(RepairWorkSerializer(repairwork)))
        return Response(new_repairworks, status=status.HTTP_201_CREATED)
    
class RepairWorkUpdateListViewSet(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request):
        for item in request.data["repairworks"]:
            if 'id' in item:
                repairwork = RepairWork.objects.get(pk=item['id'])
                serializer = RepairWorkSerializer(repairwork, data=item, partial=True)
                if serializer.is_valid():
                    serializer.save()
            else:
                serializer = RepairWorkSerializer(data=item)
                if serializer.is_valid():
                    repairwork = serializer.create(serializer.validated_data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    