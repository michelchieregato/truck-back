from __future__ import unicode_literals

from django.db import migrations
from django.contrib.auth.hashers import make_password


def add_user(apps, schema_editor):
    User = apps.get_model('user', 'User')
    user = User(email='bino@gmail.com', name='Bino', is_superuser=True, is_staff=True)
    user.password = make_password('Einstein@123')
    user.save()


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial')
    ]

    operations = [
        migrations.RunPython(
            add_user,
            reverse_code=migrations.RunPython.noop
        )
    ]