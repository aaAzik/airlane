from django.db import models

class Plane(models.Model):
    name = models.CharField(max_length=30)
    characteristics = models.CharField(max_length=30)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return self.name