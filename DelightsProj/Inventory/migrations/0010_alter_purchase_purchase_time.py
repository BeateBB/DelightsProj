# Generated by Django 5.1 on 2024-10-09 13:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0009_alter_purchase_purchase_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='purchase_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 9, 16, 5, 16, 856781)),
        ),
    ]
