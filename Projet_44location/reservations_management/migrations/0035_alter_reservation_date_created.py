# Generated by Django 3.2.7 on 2021-10-02 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations_management', '0034_auto_20211002_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
