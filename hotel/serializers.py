from rest_framework.serializers import Serializer, ModelSerializer
from . models import *
from rest_framework import serializers
from .models import Hotel
from slugify import slugify

class HotelSerializer(ModelSerializer):

    class Meta:
        model = Hotel
        fields = '__all__'


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        exclude = ('slug',)  # Исключаем поле slug, так как мы будем создавать его автоматически

    def create(self, validated_data):
        # Создаем слаг на основе имени отеля
        validated_data['slug'] = slugify(validated_data['name'])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # Обновляем слаг при обновлении данных отеля
        if 'name' in validated_data:
            validated_data['slug'] = slugify(validated_data['name'])
        return super().update(instance, validated_data)