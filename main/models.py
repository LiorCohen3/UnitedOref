from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=45, null=False)
    real_id = models.CharField(max_length=45, null=False)
    unit = models.CharField(max_length=45, null=True)
    img = models.CharField(max_length=45, null=True)

    class Meta:
        db_table = 'user'