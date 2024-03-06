# Generated by Django 5.0.1 on 2024-03-05 20:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_customuser_img_alter_customuser_unit_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requests',
            name='donate_user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='donations', to=settings.AUTH_USER_MODEL),
        ),
    ]