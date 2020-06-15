from rest_framework import serializers

from destinations.models import Destination


class DestinationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Destination
        fields = ['id', 'from_name', 'from_location', 'to_name', 'to_location', 'is_favorite', 'to_latitude', 'to_longitude',
                    'from_latitude', 'from_longitude']
        read_only_fields = ('id',)
