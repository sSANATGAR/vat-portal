# Generated by Django 5.0.6 on 2024-06-09 19:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rfid', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Firmware',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(max_length=10)),
                ('firmware_data', models.BinaryField()),
            ],
        ),
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_plate_max', models.CharField(max_length=20)),
                ('mac_address', models.CharField(max_length=12)),
                ('firmware_version', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='home.firmware')),
            ],
        ),
    ]
