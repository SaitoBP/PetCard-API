# Generated by Django 3.1.2 on 2020-10-18 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MedicationSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedule', models.DateTimeField()),
                ('cycle', models.CharField(choices=[('D', 'DAILY'), ('W', 'WEEKLY'), ('M', 'MONTHLY'), ('Y', 'YEARLY')], max_length=1)),
                ('medication_status', models.BooleanField(default=False)),
                ('medication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medication.medication')),
            ],
        ),
    ]