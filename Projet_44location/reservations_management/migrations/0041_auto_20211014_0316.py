# Generated by Django 3.2.7 on 2021-10-14 01:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservations_management', '0040_auto_20211006_2236'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='date_location_end',
        ),
        migrations.DeleteModel(
            name='Invoice',
        ),
    ]
