# Generated by Django 4.2.13 on 2024-06-21 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_firmware_firmware_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firmware',
            name='firmware_file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
