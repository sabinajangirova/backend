from django.db import models
from users.models import User
from trainstations.models import TrainStation

from django.core.validators import MaxValueValidator, MinValueValidator

class RepairWork(models.Model):
    class RepairWorkStatus(models.TextChoices):
        WAITING_FOR_CONFIRMATION = 'Waiting for confirmation'
        IN_PROGRESS = 'In progress'
        FINISHED = 'Finished'
    
    latitude = models.FloatField(validators=[MinValueValidator(-90.0), MaxValueValidator(90.0)], null=False, blank=False)
    longitude = models.FloatField(validators=[MinValueValidator(-180.0), MaxValueValidator(180.0)], null=False, blank=False)
    radius = models.IntegerField(blank=False)
    
    status = models.CharField(max_length=25, choices=RepairWorkStatus.choices, null=False, blank=False, default=RepairWorkStatus.WAITING_FOR_CONFIRMATION)
    description = models.CharField(max_length=255, null=True, blank=True, default="")
    responsible = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    # stations_around = models.ManyToManyField(TrainStation)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    expected_start_time = models.DateTimeField(null=True, blank=True)
    expected_finish_time = models.DateTimeField(null=True, blank=True)