from django.contrib import admin

from api.vaccine.models import Vaccine, VaccineSchedule

admin.site.register(Vaccine)
admin.site.register(VaccineSchedule)
