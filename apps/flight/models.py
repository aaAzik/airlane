from django.db import models
from apps.airlane.models import *
from apps.plane.models import *

class Flight(models.Model):
    From = models.CharField(max_length=30)
    To = models.CharField(max_length=30)
    plane = models.ForeignKey(Plane, on_delete=models.CASCADE, blank=True, null=True)
    airlane = models.ForeignKey(Airlane, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.From
