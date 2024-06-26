# Generated by Django 5.0.1 on 2024-02-28 17:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_requests_item_type_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donation_items',
            name='item_type_id',
        ),
        migrations.RemoveField(
            model_name='donation_items',
            name='requests_id',
        ),
        migrations.RemoveField(
            model_name='requests',
            name='donate_user_id',
        ),
        migrations.RemoveField(
            model_name='requests',
            name='item_type_id',
        ),
        migrations.RemoveField(
            model_name='requests',
            name='requests_status_id',
        ),
        migrations.AddField(
            model_name='donation_items',
            name='item_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.item_type'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='donation_items',
            name='requests',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.requests'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='requests',
            name='donate_user',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, related_name='donations', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='requests',
            name='item_type',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='main.item_type'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='requests',
            name='requests_status',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='main.request_status'),
            preserve_default=False,
        ),
    ]
