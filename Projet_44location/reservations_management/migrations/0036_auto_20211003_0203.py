# Generated by Django 3.2.7 on 2021-10-03 00:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservations_management', '0035_alter_reservation_date_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='invoice',
        ),
        migrations.AddField(
            model_name='invoice',
            name='reservation',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reservations_management.reservation'),
        ),
    ]