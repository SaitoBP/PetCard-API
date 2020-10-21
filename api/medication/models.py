from django.db import models

from dateutil.relativedelta import relativedelta


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
        next_schedule = None

        if self.cycle == 'D':
            next_schedule = self.schedule + relativedelta(days=+1)

        elif self.cycle == 'W':
            next_schedule = self.schedule + relativedelta(weeks=+1)

        elif self.cycle == 'M':
            next_schedule = self.schedule + relativedelta(months=+1)

        else:
            next_schedule = self.schedule + relativedelta(years=+1)

            """
            Debug example
            """
            # schedule = 20
            # next_schedule = schedule + 1

            # if schedule >= next_schedule:
            #     self.status = False
            #     self.save()

        if self.schedule >= next_schedule:
            self.status = False
            self.save()

        return self.status

    def __str__(self):
        return f"{self.medication} - {self.schedule}"


class Medication(models.Model):
    medicine = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.medicine
