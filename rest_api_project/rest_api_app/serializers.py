from .models import Hotel, Customer, Reservation
from rest_framework import serializers


class HotelSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100, required=True)
    country = serializers.CharField(max_length=100, required=True)
    website = serializers.CharField(max_length=100, required=True)
    city = serializers.CharField(max_length=100, required=False)

    def create(self, validated_data):
        return Hotel.objects.create(
            name=validated_data.get('name'),
            country=validated_data.get('country'),
            website=validated_data.get('website'),
            city=validated_data.get('city')
        )

    class Meta:
        model = Hotel
        fields = [
            'id',
            'name',
            'country',
            'website',
            'city'
        ]


class CustomerSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100, required=True)
    mobile = serializers.CharField(max_length=100, required=True)
    email = serializers.CharField(max_length=100, required=True)

    def create(self, validated_data):
        return Customer.objects.create(
            name=validated_data.get('name'),
            mobile=validated_data.get('mobile'),
            email=validated_data.get('email')
        )

    class Meta:
        model = Hotel
        fields = [
            'id',
            'name',
            'mobile',
            'email',
        ]


class ReservationSerializer(serializers.ModelSerializer):
    hotel_id = serializers.PrimaryKeyRelatedField(many=False, required=True)
    customer_id = serializers.PrimaryKeyRelatedField(many=False, required=True)
    number_of_rooms = serializers.IntegerField(required=True, default=1)
    checkin_date = serializers.DateField(required=True, format='iso-8601', input_formats=['iso-8601'])
    checkout_date = serializers.DateField(required=True, format='iso-8601', input_formats=['iso-8601'])

    def create(self, validated_data):
        return Reservation.objects.create(
            hotel_id=validated_data.get('hotel_id'),
            customer_id=validated_data.get('customer_id'),
            number_of_rooms=validated_data.get('number_of_rooms'),
            checkin_date=validated_data.get('checkin_date'),
            checkout_date=validated_data.get('checkout_date'),
        )

    class Meta:
        model = Hotel
        fields = [
            'id',
            'hotel_id',
            'customer_id',
            'number_of_rooms',
            'checkin_date',
            'checkout_date'
        ]

