# Generated by Django 5.1 on 2024-10-06 19:28

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0005_alter_purchase_purchase_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='purchase_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 6, 22, 27, 52, 2065)),
        ),
        migrations.RemoveField(
            model_name='reciperequirement',
            name='ingredients',
        ),
        migrations.AddField(
            model_name='reciperequirement',
            name='ingredients',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Inventory.ingredient'),
            preserve_default=False,
        ),
    ]
