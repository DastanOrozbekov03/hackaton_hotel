from django.urls import path
from .views import HotelListView, HotelDetailView

urlpatterns = [
    path('hotels/', HotelListView.as_view(), name='hotel-list'),
    path('hotels/<slug:slug>/', HotelDetailView.as_view(), name='hotel-detail'),
]