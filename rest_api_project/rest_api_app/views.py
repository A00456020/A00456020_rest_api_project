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




