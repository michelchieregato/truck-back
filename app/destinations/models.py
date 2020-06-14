from django.db import models
from user.models import User

from project import settings

class Destination(models.Model):
    to_name = models.CharField(max_length=255)
    to_location = models.CharField(max_length=255, null=True)
    from_name = models.CharField(max_length=255)
    from_location = models.CharField(max_length=255, null=True)
    is_favorite = models.BooleanField(default=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.to_name