# Generated by Django 5.1 on 2024-11-18 19:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0056_alter_purchase_purchase_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='purchase_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 18, 22, 31, 47, 542100)),
        ),
    ]