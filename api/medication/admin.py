from django.contrib import admin

from api.medication.models import Medication, MedicationSchedule

admin.site.register(Medication)
admin.site.register(MedicationSchedule)