from django.db import models
from django.conf import settings


# Create your models here
class Category(models.Model):
    """Model for category"""

    name = models.CharField(
        max_length=100,
        blank=False,
        null=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    enabled = models.BooleanField(
        default=True,
        blank=False,
        null=False
    )

    def __str__(self):
        return self.user.username + ' - ' + self.name
