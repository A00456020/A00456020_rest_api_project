from rest_framework.utils.serializer_helpers import ReturnDict

from .models import Hotel, Customer, Reservation, GuestDetails
from .serializers import HotelSerializer, CustomerSerializer, ReservationSerializer, GuestDetailsSerializer
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
        return Response(query_serializer.data, status=200)

    def post(self, request):
        hotel_serializer = HotelSerializer(data=request.data)
        if hotel_serializer.is_valid():
            new_hotel = hotel_serializer.save()
            query_serializer = HotelSerializer(new_hotel)
            return Response(query_serializer.data, status=200)
        else:
            return Response(hotel_serializer.errors, status=400)


class HotelListView(APIView):

    def get(self, request):
        queryset = Hotel.objects.all()
        query_serializer = HotelSerializer(queryset, many=True)
        return Response({"hotels_list": query_serializer.data})


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
            return Response(query_serializer.data, status=200)
        else:
            return Response(customer_serializer.errors, status=400)


class ReservationView(APIView):

    def get(self, request, id=None):
        if id:
            queryset = Reservation.objects.get(id=id)
            query_serializer = ReservationSerializer(queryset)
            query_serializer_data = query_serializer.data
            reservation_id = query_serializer_data['id']
            new_queryset = GuestDetails.objects.filter(reservation_id=reservation_id)
            new_query_serializer = GuestDetailsSerializer(new_queryset, many=True)
            new_query_serializer_data = new_query_serializer.data
            for item in new_query_serializer_data:
                del item['reservation_id']
            query_serializer_data['guest_details'] = new_query_serializer_data
            return Response(query_serializer_data)
        else:
            queryset = Reservation.objects.all()
            query_serializer = ReservationSerializer(queryset, many=True)
            query_serializer_data = query_serializer.data
            for reservation in query_serializer_data:
                reservation_id = reservation['id']
                new_queryset = GuestDetails.objects.filter(reservation_id=reservation_id)
                new_query_serializer = GuestDetailsSerializer(new_queryset, many=True)
                new_query_serializer_data = new_query_serializer.data
                for item in new_query_serializer_data:
                    del item['reservation_id']
                reservation['guest_details'] = new_query_serializer_data
            return Response(query_serializer_data)

    def post(self, request):
        if 'guest_details' not in request.data:
            err_message = "Please provide guest details, or alternatively, pass an empty list as guest_details!"
            request.data['guest_details'] = []
            # print(request.data)
            return Response({"message": err_message}, status=400)
        guest_details_request_data = request.data['guest_details']
        reservation_serializer = ReservationSerializer(data=request.data)
        if reservation_serializer.is_valid():
            print(reservation_serializer.validated_data)
            new_reservation = reservation_serializer.save()
            query_serializer = ReservationSerializer(new_reservation)
            query_serializer_data = query_serializer.data
            reservation_id = int(query_serializer_data['id'])
            for details in guest_details_request_data:
                details.update({"reservation_id": reservation_id})
                guest_details_serializer = GuestDetailsSerializer(data=details)
                if guest_details_serializer.is_valid():
                    new_guest_details = guest_details_serializer.save()
                    guest_details_query_serializer = GuestDetailsSerializer(new_guest_details)
                else:
                    return Response(guest_details_serializer.errors, status=400)
            queryset = Reservation.objects.get(id=reservation_id)
            query_serializer = ReservationSerializer(queryset)
            query_serializer_data = query_serializer.data
            reservation_id = query_serializer_data['id']
            new_queryset = GuestDetails.objects.filter(reservation_id=reservation_id)
            new_query_serializer = GuestDetailsSerializer(new_queryset, many=True)
            new_query_serializer_data = new_query_serializer.data
            for item in new_query_serializer_data:
                del item['reservation_id']
            query_serializer_data['guest_details'] = new_query_serializer_data
            return Response(query_serializer_data, status=200)
        else:
            return Response(reservation_serializer.errors, status=400)


class ReservationConfirmation(APIView):

    def post(self, request):
        reservation_serializer = ReservationSerializer(data=request.data)
        if reservation_serializer.is_valid():
            new_reservation = reservation_serializer.save()
            query_serializer = ReservationSerializer(new_reservation)
            return Response({"confirmation_number": query_serializer.data["id"]}, status=200)
        else:
            return Response(reservation_serializer.errors, status=400)




