# Generated by Django 5.0.1 on 2024-03-03 21:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_requests_requests_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='img',
            field=models.CharField(default='images/profile_img/default.png', max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='unit',
            field=models.CharField(default='UnitedOref', max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='requests',
            name='donate_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='donations', to=settings.AUTH_USER_MODEL),
        ),
    ]