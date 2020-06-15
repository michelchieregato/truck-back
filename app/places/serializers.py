from rest_framework import serializers

from .models import Place


class PlaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Place
        fields = ['name', 'rating', 'address', 'services']
        read_only_fields = ()
