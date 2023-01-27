from .models import RepairWork
from rest_framework.serializers import ModelSerializer


class RepairWorkSerializer(ModelSerializer):
    class Meta:
        model = RepairWork
        fields = ['id', 'longitude', 'latitude', 'radius', 'status', 'description', 'commenter', 'created_at', 'updated_at', 'expected_finish_time']