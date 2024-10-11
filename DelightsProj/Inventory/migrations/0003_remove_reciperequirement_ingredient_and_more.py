# Generated by Django 5.1 on 2024-10-02 05:44

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0002_purchase_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reciperequirement',
            name='ingredient',
        ),
        migrations.AddField(
            model_name='reciperequirement',
            name='ingredients',
            field=models.ManyToManyField(to='Inventory.ingredient'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='purchase_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 2, 8, 44, 41, 110610)),
        ),
        migrations.CreateModel(
            name='Calculates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.purchase')),
            ],
        ),
    ]
