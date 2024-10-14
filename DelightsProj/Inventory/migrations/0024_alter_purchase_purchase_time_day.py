# Generated by Django 5.1 on 2024-10-12 20:01

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0023_alter_purchase_purchase_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='purchase_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 12, 23, 1, 48, 536544)),
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime(2024, 10, 12, 23, 1, 48, 536545))),
                ('inventory', models.ManyToManyField(to='Inventory.ingredient')),
                ('purchases', models.ManyToManyField(to='Inventory.purchase')),
                ('summary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.daysummary')),
            ],
        ),
    ]
