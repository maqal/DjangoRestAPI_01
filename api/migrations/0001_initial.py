# Generated by Django 5.0 on 2023-12-15 11:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locationName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemName', models.CharField(max_length=50)),
                ('dateAdded', models.DateField(auto_now_add=True)),
                ('itemLocation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.location')),
            ],
        ),
    ]
