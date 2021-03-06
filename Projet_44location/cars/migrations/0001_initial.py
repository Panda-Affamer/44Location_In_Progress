# Generated by Django 3.2.7 on 2021-09-24 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('summary', models.CharField(max_length=200)),
                ('brand_image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
            options={
                'verbose_name_plural': 'Brands',
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=200)),
                ('max_speed', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('car_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('buy_date', models.DateField(blank=True, null=True)),
                ('transmission', models.CharField(blank=True, max_length=200, null=True)),
                ('carburant', models.CharField(blank=True, max_length=200, null=True)),
                ('consumption', models.CharField(blank=True, max_length=200, null=True)),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cars.brand')),
            ],
        ),
    ]
