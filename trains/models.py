from django.db import models
from users.models import User
from trainstations.models import TrainStation

class Train(models.Model):
    name = models.CharField(max_length=10, null=False, blank=False, unique=True)
    longitude = models.FloatField(null=False, blank=False)
    latitude = models.FloatField(null=False, blank=False)
    conductor = models.ForeignKey(User, related_name='conductor', on_delete=models.SET_NULL, null=True)
    departureStation = models.ForeignKey(TrainStation, related_name='departure', on_delete=models.SET_NULL, null=True, blank=False)
    destinationStation = models.ForeignKey(TrainStation, related_name='destination', on_delete=models.SET_NULL, null=True, blank=False)