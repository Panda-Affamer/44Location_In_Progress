# Generated by Django 3.2.7 on 2021-09-26 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0018_illimited_kms'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='illimited_kms',
            name='price_category',
        ),
        migrations.AddField(
            model_name='price_category',
            name='price_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cars.illimited_kms'),
        ),
    ]
