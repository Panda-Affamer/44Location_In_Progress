# Generated by Django 3.2.10 on 2022-01-02 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations_management', '0051_auto_20211031_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
