# Generated by Django 5.1 on 2024-12-10 10:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0085_alter_purchase_purchase_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='purchase_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 10, 18, 9, 4, 28051)),
        ),
    ]
