from . import views
from django.urls import path

urlpatterns = [
    path('hotels/', views.HotelView.as_view()),
    path('hotels/<int:id>/', views.HotelView.as_view()),
    path('customers/', views.CustomerView.as_view()),
    path('customers/<int:id>/', views.CustomerView.as_view()),
    path('reservations/', views.ReservationView.as_view()),
    path('', views.ReservationView.as_view()),
    path('reservations/<int:id>/', views.ReservationView.as_view()),
    path('getListOfHotels/', views.HotelListView.as_view()),
    path('getlistofhotels/', views.HotelListView.as_view()),
    path('reservationConfirmation/', views.ReservationConfirmation.as_view()),
    path('reservationconfirmation/', views.ReservationConfirmation.as_view()),
]
