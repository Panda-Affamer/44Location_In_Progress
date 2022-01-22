# Generated by Django 3.2.7 on 2021-10-04 22:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0027_alter_car_price_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='price_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cars.price_category'),
        ),
        migrations.AlterField(
            model_name='price_category',
            name='hours',
            field=models.IntegerField(blank=True, choices=[('4', '4'), ('6', '6'), ('12', '12')], null=True),
        ),
    ]