from django.db import models

# Create your models here.


class Reservation(models.Model):
    name=models.CharField(max_length=200)
    age=models.IntegerField(null=False)
    time=models.TimeField()
    note=models.TextField(max_length=200, default=None)

