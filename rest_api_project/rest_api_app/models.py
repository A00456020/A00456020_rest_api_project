from django.db import models


class Hotel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    country = models.CharField(max_length=100, null=False, blank=False)
    website = models.CharField(max_length=100, null=False, blank=False)
    city = models.CharField(max_length=100, null=True, blank=False)
    price = models.FloatField(default=250, null=False)
    availability = models.BooleanField(default=True, null=False)


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    mobile = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=False, blank=False)


class Reservation(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    number_of_rooms = models.IntegerField(null=False, default=1, blank=False)
    checkin_date = models.DateField(null=False, blank=False)
    checkout_date = models.DateField(null=False, blank=False)
    hotel_name = models.CharField(max_length=100, null=True)
    customer_name = models.CharField(max_length=100, null=True)
    customer_phone = models.CharField(max_length=100, null=True)
    hotel_website = models.CharField(max_length=100, null=True)


class GuestDetails(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=100, null=False, blank=False)
    gender = models.CharField(max_length=100, null=False, blank=False, default="male")
    email = models.CharField(max_length=100, null=True, blank=False)
    mobile = models.CharField(max_length=100, null=True, blank=False)
