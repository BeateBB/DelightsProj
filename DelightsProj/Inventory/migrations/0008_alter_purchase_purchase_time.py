# Generated by Django 5.1 on 2024-10-09 12:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0007_rename_ingredients_reciperequirement_ingredient_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='purchase_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 9, 15, 27, 2, 34021)),
        ),
    ]
