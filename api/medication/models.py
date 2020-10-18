from django.db import models


class MedicationSchedule(models.Model):
    CYCLE_CHOICES = [
        ('D', 'DAILY'),
        ('W', 'WEEKLY'),
        ('M', 'MONTHLY'),
        ('Y', 'YEARLY')

    ]

    medication = models.ForeignKey('Medication', related_name='medication_schedule', on_delete=models.CASCADE)
    schedule = models.DateTimeField()
    cycle = models.CharField(max_length=1, choices=CYCLE_CHOICES)
    medication_status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.medication} - {self.schedule}"


class Medication(models.Model):
    medicine = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.medicine
