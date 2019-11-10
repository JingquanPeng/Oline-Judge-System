# --coding:GBK--

from django.db import models


# Create your models here.

# create class corresponding to database tables
class User(models.Model):
    username = models.CharField(max_length=20, blank=False, null=False)
    password = models.CharField(max_length=10, blank=False, null=False)


class PurchaseRecord(models.Model):
    username = models.CharField(max_length=20, blank=False, null=False)
    date = models.DateField()
    description = models.CharField(max_length=250)
    money = models.DecimalField(max_digits=5, decimal_places=2)
    type = models.PositiveSmallIntegerField()


class ParkingRecord(models.Model):
    plateNumber = models.CharField(max_length=8, blank=False, null=False)
    entrance = models.PositiveSmallIntegerField(null=False)
    arrivalDate = models.DateField(max_length=10, blank=False, null=False)
    arrivalTime = models.CharField(max_length=5, blank=False, null=False)
    staffName = models.CharField(max_length=10, blank=False, null=False)
    status = models.CharField(max_length=3, null=False)
