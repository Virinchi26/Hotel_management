# Generated by Django 4.2.7 on 2024-04-10 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_management', '0011_contactmessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='total_amount',
            field=models.FloatField(default=0.0),
        ),
    ]
