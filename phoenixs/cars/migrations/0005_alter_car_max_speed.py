# Generated by Django 4.2.2 on 2023-07-02 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_car_horsepower_car_max_speed_car_overclocking_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='max_speed',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
