# Generated by Django 4.2.2 on 2023-07-15 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0013_remove_car_exclusive'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]