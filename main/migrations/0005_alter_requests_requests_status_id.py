# Generated by Django 5.0.1 on 2024-02-20 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_requests_area_alter_requests_info_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requests',
            name='requests_status_id',
            field=models.IntegerField(default=2),
        ),
    ]