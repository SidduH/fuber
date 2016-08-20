from django.db import models


class Cabs(models.Model):
    cab_id = models.IntegerField(primary_key=True)
    owner_name = models.CharField(max_length=100)
    lattitude = models.FloatField()
    longitude = models.FloatField()
    status = models.BooleanField()
    cab_type = models.CharField()


class Customer(models.Model):
    cust_id = models.IntegerField(primary_key=True)
    cust_name = models.CharField(max_length=200)


class Rides(models.Model):
    cab_id = models.ForeignKey(Cabs)
    cust_id = models.ForeignKey(Customer)
    start_lattitude = models.FloatField()
    start_longitude = models.FloatField()
    stop_lattitude = models.FloatField()
    stop_longitude = models.FloatField()

