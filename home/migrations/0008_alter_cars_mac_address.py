# Generated by Django 4.2.13 on 2024-07-13 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_cars_mac_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='mac_address',
            field=models.CharField(db_index=True, max_length=17),
        ),
    ]
