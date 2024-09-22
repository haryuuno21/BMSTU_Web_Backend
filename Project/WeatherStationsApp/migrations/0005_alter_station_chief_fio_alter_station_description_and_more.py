# Generated by Django 5.1.1 on 2024-09-21 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WeatherStationsApp', '0004_rename_adress_station_address_remove_station_photo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station',
            name='chief_fio',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='station',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='station',
            name='phone_number',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
