# Generated by Django 3.0.7 on 2020-06-14 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_auto_20200614_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='services',
            field=models.ManyToManyField(blank=True, to='places.Service'),
        ),
    ]
