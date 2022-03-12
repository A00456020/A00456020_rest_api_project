from . import views
from django.urls import path

urlpatterns = [
    path('hotels/', views.HotelView.as_view()),
    path('hotels/<int:id>/', views.HotelView.as_view()),
    path('customers/', views.CustomerView.as_view()),
    path('customers/<int:id>/', views.CustomerView.as_view()),
    path('reservations/', views.ReservationView.as_view()),
    path('reservations/<int:id>/', views.ReservationView.as_view())
]
