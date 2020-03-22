from django.db import models
from datetime import datetime

class Tech(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=75)
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=75)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.name