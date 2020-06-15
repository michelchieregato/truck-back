from django.db import models

from user.models import User
from project import settings


class Service(models.Model):

    HEALTH_SERVICE = 1
    HYGIENE_SERVICE = 2
    FOOD_SERVICE = 3
    REST_SERVICE = 4
    SAFETY_SERVICE = 5

    TYPES_OF_SERVICE = (
        (HEALTH_SERVICE, 'health'),
        (HYGIENE_SERVICE, 'hygiene'),
        (FOOD_SERVICE, 'food'),
        (REST_SERVICE, 'rest'),
        (SAFETY_SERVICE, 'safety')
    )

    name = models.CharField(max_length=100)
    service_type = models.SmallIntegerField(choices=TYPES_OF_SERVICE)

    def __str__(self):
        return '{} of type {}'.format(self.name, self.service_type)


class Place(models.Model):

    STARS = (
        (1, 'ONE STAR'),
        (2, 'TWO STARS'),
        (3, 'THREE STARS'),
        (4, 'FOUR STARS'),
        (5, 'FIVE STARS')
    )

    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    rating = models.SmallIntegerField(choices=STARS)
    address = models.CharField(max_length=200)
    services = models.ManyToManyField(Service, blank=True)
    image_name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    comment = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)

    def __str__(self):
        return self.place.name
