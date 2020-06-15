from django.shortcuts import render

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication

from rest_framework import viewsets
from places.models import Place
from .serializers import PlaceSerializer


class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        return self.queryset


# Create your views here.
