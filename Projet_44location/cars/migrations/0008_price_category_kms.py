# Generated by Django 3.2.7 on 2021-09-26 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0007_remove_price_kms'),
    ]

    operations = [
        migrations.AddField(
            model_name='price_category',
            name='kms',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
