# Generated by Django 3.0.6 on 2020-06-08 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_remove_userprofile_following'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserLog',
        ),
    ]
