from django.urls import path

from . import views

app_name = 'places'

urlpatterns = [
    path('', views.PlaceViewSet.as_view({'get': 'list'}))
]