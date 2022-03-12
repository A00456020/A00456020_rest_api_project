from django.shortcuts import render
from django.http import HttpResponse
from .models import Hotel, Customer, Reservation
from .serializers import HotelSerializer, CustomerSerializer, ReservationSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


class HotelView(APIView):

    def get(self, request, id=None):
        if id:
            queryset = Hotel.objects.get(id=id)
            query_serializer = HotelSerializer(queryset)
        else:
            queryset = Hotel.objects.all()
            query_serializer = HotelSerializer(queryset, many=True)
        return Response(query_serializer.data)

    def post(self, request):
        hotel_serializer = HotelSerializer(data=request.data)
        if hotel_serializer.is_valid():
            new_hotel = hotel_serializer.save()
            query_serializer = HotelSerializer(new_hotel)
            return Response(query_serializer.data, status=201)
        else:
            return Response(hotel_serializer.errors, status=400)


class CustomerView(APIView):

    def get(self, request, id=None):
        if id:
            queryset = Customer.objects.get(id=id)
            query_serializer = CustomerSerializer(queryset)
        else:
            queryset = Customer.objects.all()
            query_serializer = CustomerSerializer(queryset, many=True)
        return Response(query_serializer.data)

    def post(self, request):
        customer_serializer = CustomerSerializer(data=request.data)
        if customer_serializer.is_valid():
            new_customer = customer_serializer.save()
            query_serializer = CustomerSerializer(new_customer)
            return Response(query_serializer.data, status=201)
        else:
            return Response(customer_serializer.errors, status=400)


class ReservationView(APIView):

    def get(self, request, id=None):
        if id:
            queryset = Reservation.objects.get(id=id)
            query_serializer = ReservationSerializer(queryset)
        else:
            queryset = Reservation.objects.all()
            query_serializer = ReservationSerializer(queryset, many=True)
        return Response(query_serializer.data)

    def post(self, request):
        reservation_serializer = ReservationSerializer(data=request.data)
        if reservation_serializer.is_valid():
            new_reservation = reservation_serializer.save()
            query_serializer = ReservationSerializer(new_reservation)
            return Response(query_serializer.data, status=201)
        else:
            return Response(reservation_serializer.errors, status=400)




