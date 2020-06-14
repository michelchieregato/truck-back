from rest_framework import serializers

from destinations.models import Destination


class DestinationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Destination
        fields = ['id', 'from_name', 'from_location', 'to_name', 'to_location', 'is_favorite']
        read_only_fields = ('id',)
