# Generated by Django 3.1.2 on 2020-10-18 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vaccine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vaccine', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='VaccineSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedule', models.DateTimeField()),
                ('status', models.BooleanField(default=False)),
                ('cycle', models.CharField(choices=[('D', 'DAILY'), ('W', 'WEEKLY'), ('M', 'MONTHLY'), ('Y', 'YEARLY')], default='D', max_length=1)),
                ('vaccine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vaccine_schedule', to='vaccine.vaccine')),
            ],
        ),
    ]
