# Generated by Django 4.2.2 on 2023-07-02 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0006_alter_car_max_speed_alter_car_overclocking'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
