# Generated by Django 5.0.1 on 2024-02-20 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_requests_area_alter_requests_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requests',
            name='area',
            field=models.CharField(default=None, max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='requests',
            name='info',
            field=models.CharField(default=None, max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='requests',
            name='location_lat',
            field=models.FloatField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='requests',
            name='location_long',
            field=models.FloatField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='requests',
            name='schedule_date',
            field=models.DateField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='requests',
            name='schedule_time',
            field=models.TimeField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='requests',
            name='type_id',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='requests',
            name='unit',
            field=models.CharField(default=None, max_length=45, null=True),
        ),
    ]
