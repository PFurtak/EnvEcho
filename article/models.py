from django.db import models
from datetime import datetime
from techs.models import Tech

class Article(models.Model):
    tech = models.ForeignKey(Tech, on_delete=models.DO_NOTHING)
    create_date = models.DateTimeField(default=datetime.now, blank=True)
    title = models.CharField(max_length=250)
    type = models.CharField(max_length=250)
    vendor = models.CharField(max_length=250)
    purchase_date = models.DateTimeField(default=datetime.now, blank=True)
    expire_date = models.DateTimeField(default=datetime.now, blank=True)
    serial = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    is_published = models.BooleanField(default=True)
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    def __str__(self):
        return self.title


    
