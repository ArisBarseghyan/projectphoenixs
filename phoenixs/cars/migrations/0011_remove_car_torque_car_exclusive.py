# Generated by Django 4.2.2 on 2023-07-03 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0010_remove_car_model3d_car_body_type_car_engine_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='torque',
        ),
        migrations.AddField(
            model_name='car',
            name='exclusive',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
