# Generated by Django 5.1 on 2024-10-21 15:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0041_alter_purchase_purchase_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='day',
            name='today_ingredients',
            field=models.ManyToManyField(to='Inventory.ingredient'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='purchase_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 21, 18, 53, 25, 81127)),
        ),
    ]
