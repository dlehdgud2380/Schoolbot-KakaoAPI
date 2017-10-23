from django.db import models
from django.conf import settings
import datetime
from pytz import timezone

# Create your models here.

class School_Info(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    img = models.ImageField(upload_to='img/%Y/%m/%d/')
    comment = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title