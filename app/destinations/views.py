from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets, mixins, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from destinations.models import Destination
from destinations import serializers


class DestinationViewSet(viewsets.GenericViewSet, 
                         mixins.ListModelMixin, 
                         mixins.CreateModelMixin,
                         filters.BaseFilterBackend):
    authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    queryset = Destination.objects.all()
    serializer_class = serializers.DestinationSerializer

    def get_queryset(self):
        """Return objects for authenticated users only"""
        is_favorite = self.request.query_params.get('is_favorite', None)
        if is_favorite is not None:
            return self.queryset.filter(user=self.request.user.id, is_favorite=True).order_by('-created_at')
        return self.queryset.filter(user=self.request.user.id).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def retrieve(self, request, pk=None):
        destination = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(destination)
        return Response(serializer.data)
