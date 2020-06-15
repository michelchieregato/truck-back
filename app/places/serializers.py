from rest_framework import serializers

from .models import Place, Service

class ServiceSerializer(serializers.ModelSerializer):
    service_type = serializers.CharField(source='get_service_type_display')
    class Meta:
        model = Service
        fields = ['name', 'service_type']
        read_only_fields = ()


class PlaceSerializer(serializers.ModelSerializer):
    services = ServiceSerializer(read_only=True, many=True)

    class Meta:
        model = Place
        fields = ['name', 'rating', 'address', 'services', 'image_name']
        read_only_fields = ()

