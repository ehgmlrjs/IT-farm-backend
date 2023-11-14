from django.db import models

# Create your models here.
class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    photo = models.CharField(max_length=255, default='')
    regdate = models.DateTimeField()
    enddate = models.DateTimeField()
