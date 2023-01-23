from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .models import RepairWork
from rest_framework.response import Response
from users.models import User

class RepairWorkCreateView(CreateAPIView):
    def create(self, request, *args, **kwargs):
        longitude = request.data["longitude"]
        latitude = request.data["latitude"]
        radius = request.data["radius"]
        commenter = 1
        user = User.objects.get(pk=1)
        repairwork = RepairWork.objects.create(longitude=longitude,latitude=latitude,radius=radius,commenter=user)
        return Response("Repairment work created successfully", status=201)
        # return super().create(request, *args, **kwargs)
