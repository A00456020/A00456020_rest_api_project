from . import views
from django.urls import path

urlpatterns = [
    path('hotels/', views.HotelView.as_view()),
    path('hotels/<int:id>/', views.HotelView.as_view())
]
