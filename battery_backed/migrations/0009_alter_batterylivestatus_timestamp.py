# Generated by Django 4.2.11 on 2024-08-27 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battery_backed', '0008_batterylivestatus_devid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batterylivestatus',
            name='timestamp',
            field=models.DateTimeField(),
        ),
    ]
