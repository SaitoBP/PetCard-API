from django.db import models

from api.pet.models import Pet

from datetime import datetime, timezone
from dateutil.relativedelta import relativedelta


class Medication(models.Model):
    medicine = models.CharField(max_length=255)
    description = models.TextField()

    pet = models.ForeignKey(Pet, related_name='pet_medication', on_delete=models.CASCADE)

    def __str__(self):
        return self.medicine


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
    status = models.BooleanField(default=False)

    @property
    def validate_status(self):

        """
        Auto 'today' variable
        """
        # today = datetime.now()

        """
        Debug 'today' variable
        """
        today = datetime(2020, 10, 21, tzinfo=timezone.utc)

        if self.cycle == 'D':
            next_schedule = self.schedule + relativedelta(days=+1)

        elif self.cycle == 'W':
            next_schedule = self.schedule + relativedelta(weeks=+1)

        elif self.cycle == 'M':
            next_schedule = self.schedule + relativedelta(months=+1)

        else:
            next_schedule = self.schedule + relativedelta(years=+1)

        if today >= self.schedule:
            # Reset status back to False
            self.status = False

            # Change the schedule date to the next_schedule so the cycle can continue
            self.schedule = next_schedule

            # Save changes
            self.save()

        return self.status

    def __str__(self):
        return f"{self.medication} - {self.schedule}"
