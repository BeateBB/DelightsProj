# Generated by Django 5.1 on 2024-11-24 12:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0068_alter_purchase_purchase_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='purchase_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 24, 19, 15, 29, 262593)),
        ),
    ]