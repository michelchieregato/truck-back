# Generated by Django 3.0.7 on 2020-06-14 22:28

from django.db import migrations

def create_services(apps, schema_editor):
    Service = apps.get_model('places', 'Service')
    Service.objects.create(name='Alimentação', service_type=3)
    Service.objects.create(name='Saúde', service_type=1)
    Service.objects.create(name='Chuveiro', service_type=2)
    Service.objects.create(name='Alojamento', service_type=4)
    Service.objects.create(name='Políca', service_type=5)


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_place_services'),
    ]

    operations = [
        migrations.RunPython(create_services)
    ]
