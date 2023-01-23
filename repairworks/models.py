from django.db import models
from users.models import User

class RepairWork(models.Model):
    # repair_location = md.PointField(blank=False)
    longitude = models.FloatField(null=False, blank=False)
    latitude = models.FloatField(null=False, blank=False)
    radius = models.IntegerField(blank=False)
    description = models.CharField(max_length=255, null=True, blank=True, default="")
    commenter = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)