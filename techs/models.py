from django.db import models
from datetime import datetime

class Tech(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    position = models.CharField(max_length=75)
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=75)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.username