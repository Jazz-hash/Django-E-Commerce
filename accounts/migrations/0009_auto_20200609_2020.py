# Generated by Django 3.0.6 on 2020-06-09 15:20

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20200609_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None),
        ),
    ]
