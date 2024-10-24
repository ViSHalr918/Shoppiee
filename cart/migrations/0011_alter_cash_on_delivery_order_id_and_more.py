# Generated by Django 5.1.2 on 2024-10-22 05:23

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0010_alter_cash_on_delivery_order_id_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='cash_on_delivery',
            name='order_id',
            field=models.UUIDField(default=uuid.UUID('a7225bb7-0866-47a4-8476-ab1d108c4c65'), null=True),
        ),
        migrations.AlterField(
            model_name='cash_on_delivery',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cash', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='cash_on_delivery',
            name='product_object',
            field=models.ManyToManyField(to='cart.product'),
        ),
    ]
