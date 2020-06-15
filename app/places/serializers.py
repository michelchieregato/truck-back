from rest_framework import serializers

from .models import Place


class PlaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Place
        fields = []
        read_only_fields = ()
