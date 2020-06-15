from django.shortcuts import render
from math import pi, sin, cos, sqrt, atan2

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication

from rest_framework import viewsets
from places.models import Place
from .serializers import PlaceSerializer

EARTH_RADIUS = 6371


class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        return self.queryset

    def get_distance(self, ref, dest):
        ref_lat = self.degrees_to_rad(ref.latitude)
        dest_lat = self.degrees_to_rad(dest.latitude)
        dLat = self.degrees_to_rad(dest.latitude - ref.latitude)
        dLong = self.degrees_to_rad(dest.longitude - ref.longitude)
        a = sin(dLat / 2) ** 2 + (sin(dLong) ** 2) * cos(ref_lat) * cos(dest_lat)
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        return EARTH_RADIUS * c

    def degrees_to_rad(self, angle):
        return angle * pi / 180


# Create your views here.
