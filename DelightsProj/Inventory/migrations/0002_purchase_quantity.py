# Generated by Django 5.1 on 2024-09-24 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
