from django.db import models

class Cabs(models.Model):
    cab_id = models.IntegerField(primary_key=True)
    owner_name = models.CharField(max_length=100)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    status = models.CharField(max_length=50)  # free or booked
    cab_type = models.CharField(max_length=100)  # Pink or not

    def __str__(self):
        return self.owner_name


class Customer(models.Model):
    cust_id = models.IntegerField(primary_key=True)
    cust_name = models.CharField(max_length=200)

    def __str__(self):
        return self.cust_name


class Rides(models.Model):
    cab_id = models.ForeignKey(Cabs, on_delete=models.CASCADE)
    cust_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    start_latitude = models.FloatField()
    start_longitude = models.FloatField()
    stop_latitude = models.FloatField()
    stop_longitude = models.FloatField()

