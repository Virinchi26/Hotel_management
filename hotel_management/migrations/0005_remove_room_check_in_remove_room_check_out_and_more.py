# Generated by Django 4.2.4 on 2023-11-03 05:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_management', '0004_room_check_in_room_check_out_reservation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='check_in',
        ),
        migrations.RemoveField(
            model_name='room',
            name='check_out',
        ),
        migrations.DeleteModel(
            name='Reservation',
        ),
    ]
