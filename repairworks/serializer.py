from .models import RepairWork
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


class RepairWorkSerializer(ModelSerializer):
    class Meta:
        model = RepairWork
        fields = ['id', 'longitude', 'latitude', 'radius', 'status', 'description', 'responsible', 'created_at', 'updated_at', 'expected_start_time', 'expected_finish_time']