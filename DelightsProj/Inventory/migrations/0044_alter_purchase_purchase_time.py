# Generated by Django 5.1 on 2024-10-22 09:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0043_delete_daysummary_day_num_purchases_day_total_cost_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='purchase_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 22, 12, 45, 32, 214866)),
        ),
    ]