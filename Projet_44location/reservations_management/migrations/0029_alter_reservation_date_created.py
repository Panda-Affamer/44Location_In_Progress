# Generated by Django 3.2.7 on 2021-09-28 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations_management', '0028_auto_20210928_0048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='date_created',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
