# Generated by Django 3.1.2 on 2020-10-20 22:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medication', '0002_auto_20201018_1656'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medicationschedule',
            old_name='medication_status',
            new_name='status',
        ),
    ]
