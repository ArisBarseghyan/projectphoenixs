# Generated by Django 4.2.2 on 2023-07-03 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0008_company_country_company_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='model3d',
            field=models.FileField(blank=True, null=True, upload_to='3d_models/'),
        ),
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='logo/'),
        ),
    ]
