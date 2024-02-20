from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=45, null=False)
    real_id = models.CharField(max_length=45, null=False)
    unit = models.CharField(max_length=45, null=True)
    img = models.CharField(max_length=45, null=True)

    class Meta:
        db_table = 'user'


class request_type(models.Model):
    type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=45)


class item_type(models.Model):
    item_type_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=45)
    request_type = models.IntegerField(default=2)  # Assuming default value is 2


class request_status(models.Model):
    request_status_id = models.AutoField(primary_key=True)
    request_status_name = models.CharField(max_length=45, null=False)


class requests(models.Model):
    requests_id = models.AutoField(primary_key=True)
    requests_status_id = models.IntegerField(default=2)
    donate_user_id = models.IntegerField(default=0)
    receive_user_id = models.IntegerField(null=False)
    location_lat = models.FloatField(default=None, null=True)
    location_long = models.FloatField(default=None, null=True)
    area = models.CharField(max_length=45, default=None, null=True)
    info = models.CharField(max_length=45, default=None, null=True)
    type_id = models.IntegerField(default=None, null=True)
    unit = models.CharField(max_length=45, default=None, null=True)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    schedule_date = models.DateField(default=None, null=True)
    schedule_time = models.TimeField(default=None, null=True)


class unit_img(models.Model):
    u_img_id = models.AutoField(primary_key=True)
    img_url = models.CharField(max_length=45, default='default.png', null=False)
    unit_name = models.CharField(max_length=45, null=True)


class donation_items(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=45, null=False)
    item_quantity = models.IntegerField(default=1, null=False)
    item_quantity_received = models.IntegerField(default=0, null=False)
    item_type_id = models.IntegerField(null=True)
    requests_id = models.IntegerField(null=True)
