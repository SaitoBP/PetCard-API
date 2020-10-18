from django.db import models


class MedicationSchedule(models.Model):
    CYCLE_CHOICES = [
        ('D', 'DAILY'),
        ('W', 'WEEKLY'),
        ('M', 'MONTHLY'),
        ('Y', 'YEARLY')

    ]

    medication_schedule = models.DateTimeField()
    cycle = models.CharField(max_length=1, choices=CYCLE_CHOICES)
    medication_status = models.BooleanField(default=False)


class Medication(models.Model):
    medicine = models.CharField(max_length=255)
    medication_schedule = models.ForeignKey(MedicationSchedule, on_delete=models.CASCADE)
