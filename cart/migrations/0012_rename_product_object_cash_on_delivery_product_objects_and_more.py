# Generated by Django 5.1.2 on 2024-10-22 05:25

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0011_alter_cash_on_delivery_order_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cash_on_delivery',
            old_name='product_object',
            new_name='product_objects',
        ),
        migrations.AlterField(
            model_name='cash_on_delivery',
            name='order_id',
            field=models.UUIDField(default=uuid.UUID('5a07a52e-f946-4e36-a13f-e63f9410e229'), null=True),
        ),
    ]
