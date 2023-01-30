from django.db import models
from users.models import User

from django.core.validators import MaxValueValidator, MinValueValidator

class TrainStation(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, unique=True)
    latitude = models.FloatField(validators=[MinValueValidator(-90.0), MaxValueValidator(90.0)], null=False, blank=False)
    longitude = models.FloatField(validators=[MinValueValidator(-180.0), MaxValueValidator(180.0)], null=False, blank=False)
    administrator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name