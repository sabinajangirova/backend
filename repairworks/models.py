from django.db import models
from users.models import User

class RepairWork(models.Model):
    class RepairWorkStatus(models.TextChoices):
        WAITING_FOR_CONFIRMATION = 'Waiting for confirmation'
        IN_PROGRESS = 'In progress'
        FINISHED = 'Finished'
    
    longitude = models.FloatField(null=False, blank=False)
    latitude = models.FloatField(null=False, blank=False)
    radius = models.IntegerField(blank=False)
    status = models.CharField(max_length=25, choices=RepairWorkStatus.choices, null=False, blank=False, default=RepairWorkStatus.WAITING_FOR_CONFIRMATION)
    description = models.CharField(max_length=255, null=True, blank=True, default="")
    commenter = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    expected_finish_time = models.DateTimeField(null=True, blank=True)