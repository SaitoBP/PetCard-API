from django.db import models

from datetime import datetime, timezone
from dateutil.relativedelta import relativedelta


class Vaccine(models.Model):
    vaccine = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f'{self.vaccine}'


class VaccineSchedule(models.Model):
    CYCLE_CHOICES = [
        ('D', 'DAILY'),
        ('W', 'WEEKLY'),
        ('M', 'MONTHLY'),
        ('Y', 'YEARLY')
    ]

    vaccine = models.ForeignKey(Vaccine, related_name='vaccine_schedule', on_delete=models.CASCADE)
    schedule = models.DateTimeField()
    status = models.BooleanField(default=False)
    cycle = models.CharField(max_length=1, choices=CYCLE_CHOICES, default='D')

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
        return f'{self.vaccine} - {self.schedule}'
