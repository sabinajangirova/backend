from django.db import models
from users.models import User
from trainstations.models import TrainStation

from django.core.validators import MaxValueValidator, MinValueValidator

class Train(models.Model):
    name = models.CharField(max_length=10, null=False, blank=False, unique=True)
    latitude = models.FloatField(validators=[MinValueValidator(-90.0), MaxValueValidator(90.0)], null=False, blank=False)
    longitude = models.FloatField(validators=[MinValueValidator(-180.0), MaxValueValidator(180.0)], null=False, blank=False)
    
    conductor = models.ForeignKey(User, related_name='conductor', on_delete=models.SET_NULL, null=True)
    
    departureStation = models.ForeignKey(TrainStation, related_name='departureStation', on_delete=models.SET_NULL, null=True, blank=False)
    destinationStation = models.ForeignKey(TrainStation, related_name='destinationStation', on_delete=models.SET_NULL, null=True, blank=False)