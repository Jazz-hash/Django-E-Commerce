# Generated by Django 3.0.6 on 2020-06-07 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0008_item_accessory'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessaryLabel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AlterField(
            model_name='item',
            name='colors',
            field=models.ManyToManyField(blank=True, to='items.Colour'),
        ),
        migrations.AlterField(
            model_name='item',
            name='label',
            field=models.ManyToManyField(blank=True, to='items.Label'),
        ),
        migrations.AlterField(
            model_name='item',
            name='sizes',
            field=models.ManyToManyField(blank=True, to='items.Size'),
        ),
        migrations.AddField(
            model_name='item',
            name='accessory_label',
            field=models.ManyToManyField(blank=True, to='items.AccessaryLabel'),
        ),
    ]
