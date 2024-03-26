# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Hotel
from .serializers import HotelSerializer

class HotelListView(APIView):
    def get(self, request):
        hotels = Hotel.objects.all()
        serializer = HotelSerializer(hotels, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = HotelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HotelDetailView(APIView):
    def get_object(self, slug):
        try:
            return Hotel.objects.get(slug=slug)
        except Hotel.DoesNotExist:
            return None

    def get(self, request, slug):
        hotel = self.get_object(slug)
        if hotel:
            serializer = HotelSerializer(hotel)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, slug):
        hotel = self.get_object(slug)
        if hotel:
            serializer = HotelSerializer(hotel, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, slug):
        hotel = self.get_object(slug)
        if hotel:
            hotel.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
