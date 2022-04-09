from .models import Hotel, Customer, Reservation, GuestDetails
from rest_framework import serializers


class HotelSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100, required=True)
    country = serializers.CharField(max_length=100, required=True)
    website = serializers.CharField(max_length=100, required=True)
    city = serializers.CharField(max_length=100, required=False)
    price = serializers.FloatField(required=False, default=250)
    availability = serializers.BooleanField(default=True, required=False)

    def create(self, validated_data):
        return Hotel.objects.create(
            name=validated_data.get('name'),
            country=validated_data.get('country'),
            website=validated_data.get('website'),
            city=validated_data.get('city'),
            price=validated_data.get('price'),
            availability=validated_data.get('availability')
        )

    class Meta:
        model = Hotel
        fields = [
            'id',
            'name',
            'country',
            'website',
            'city',
            'price',
            'availability'
        ]


class CustomerSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100, required=True)
    mobile = serializers.CharField(max_length=100, required=False)
    email = serializers.CharField(max_length=100, required=True)

    def create(self, validated_data):
        return Customer.objects.create(
            name=validated_data.get('name'),
            mobile=validated_data.get('mobile'),
            email=validated_data.get('email')
        )

    class Meta:
        model = Customer
        fields = [
            'id',
            'name',
            'mobile',
            'email',
        ]


class ReservationSerializer(serializers.ModelSerializer):
    # hotel_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    # customer_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    hotel_id = serializers.IntegerField(required=True)
    customer_id = serializers.IntegerField(required=True)
    number_of_rooms = serializers.IntegerField(default=1)
    checkin_date = serializers.DateField(required=True, format='iso-8601', input_formats=['iso-8601'])
    checkout_date = serializers.DateField(required=True, format='iso-8601', input_formats=['iso-8601'])

    def create(self, validated_data):
        return Reservation.objects.create(
            hotel_id=validated_data.get('hotel_id'),
            customer_id=validated_data.get('customer_id'),
            hotel_name=str(Hotel.objects.get(id=validated_data.get('hotel_id')).name),
            customer_name=str(Customer.objects.get(id=validated_data.get('customer_id')).name),
            hotel_website=str(Hotel.objects.get(id=validated_data.get('hotel_id')).website),
            customer_phone=str(Customer.objects.get(id=validated_data.get('customer_id')).mobile),
            number_of_rooms=validated_data.get('number_of_rooms'),
            checkin_date=validated_data.get('checkin_date'),
            checkout_date=validated_data.get('checkout_date'),
        )

    class Meta:
        model = Reservation
        fields = [
            'id',
            'hotel_id',
            'customer_id',
            'hotel_name',
            'customer_name',
            'customer_phone',
            'hotel_website',
            'number_of_rooms',
            'checkin_date',
            'checkout_date'
        ]


class GuestDetailsSerializer(serializers.ModelSerializer):
    reservation_id = serializers.IntegerField(required=True)
    name = serializers.CharField(max_length=100, required=True)
    gender = serializers.CharField(max_length=100, required=True)
    mobile = serializers.CharField(max_length=100, required=False)
    email = serializers.CharField(max_length=100, required=False)

    def create(self, validated_data):
        return GuestDetails.objects.create(
            reservation_id=validated_data.get('reservation_id'),
            name=validated_data.get('name'),
            gender=validated_data.get('gender'),
            mobile=validated_data.get('mobile'),
            email=validated_data.get('email')
        )

    class Meta:
        model = GuestDetails
        fields = [
            'reservation_id',
            'name',
            'gender',
            'mobile',
            'email'
        ]


