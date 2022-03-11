from django.db import models


class Hotel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    country = models.CharField(max_length=100, null=False)
    website = models.CharField(max_length=100, null=False)
    city = models.CharField(max_length=100, null=True)


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    mobile = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=100, null=False)


class Reservation(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    number_of_rooms = models.IntegerField(null=False, default=1)
    checkin_date = models.DateField(null=False)
    checkout_date = models.DateField(null=False)
