from django.db import models


class MedicationSchedule(models.Model):
    CYCLE_CHOICES = [
        ('D', 'DAILY'),
        ('W', 'WEEKLY'),
        ('M', 'MONTHLY'),
        ('Y', 'YEARLY')

    ]

    schedule = models.DateTimeField()
    cycle = models.CharField(max_length=1, choices=CYCLE_CHOICES)
    medication_status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.schedule} - {self.cycle} - [{self.medication_status}]"


class Medication(models.Model):
    medicine = models.CharField(max_length=255)
    description = models.TextField()
    medication_schedule = models.ForeignKey(MedicationSchedule, on_delete=models.CASCADE)

    def __str__(self):
        return self.medicine
