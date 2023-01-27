from django.db import models
from users.models import User

class TrainStation(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, unique=True)
    longitude = models.FloatField(null=False, blank=False)
    latitude = models.FloatField(null=False, blank=False)
    administrator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name