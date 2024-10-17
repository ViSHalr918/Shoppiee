# Generated by Django 5.1.2 on 2024-10-17 01:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_address_area'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='user_object',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detail', to=settings.AUTH_USER_MODEL),
        ),
    ]