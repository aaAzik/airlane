from django.db import models
from apps.plane.models import *

class Airlane(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateField(auto_now=True)
    planes = models.ManyToManyField(Plane, blank=True, null=True)

    def __str__(self):
        return self.name
