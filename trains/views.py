from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from trains.serializer import TrainSerializer

from .models import Train

class TrainsListViewSet(ListCreateAPIView):
    serializer_class = TrainSerializer
    permission_classes = [IsAuthenticated]
    # permission_classes = []

    def get_queryset(self):
        queryset = Train.objects.all()
        user=self.request.GET.get('user')
        if user is not None:
            queryset = queryset.filter(conductor=user)
        return queryset

class TrainViewSet(RetrieveUpdateDestroyAPIView):
    queryset = Train.objects.all()
    serializer_class = TrainSerializer
    serializer = TrainSerializer(queryset, many=True)

    permission_classes = [IsAuthenticated]
    # permission_classes = []
    
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)




