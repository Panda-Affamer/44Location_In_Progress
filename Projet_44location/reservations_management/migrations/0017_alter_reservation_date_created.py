# Generated by Django 3.2.7 on 2021-09-26 16:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('reservations_management', '0016_alter_reservation_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 9, 26, 16, 37, 42, 709467, tzinfo=utc), null=True),
        ),
    ]
