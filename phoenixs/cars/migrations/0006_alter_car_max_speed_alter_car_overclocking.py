# Generated by Django 4.2.2 on 2023-07-02 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_alter_car_max_speed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='max_speed',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='overclocking',
            field=models.FloatField(blank=True, null=True),
        ),
    ]