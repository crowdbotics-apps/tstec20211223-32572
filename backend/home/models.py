from django.conf import settings
from django.db import models


class Test(models.Model):
    "Generated Model"
    firstName = models.TextField()
    boolean = models.CharField(
        max_length=256,
    )
