from rest_framework import viewsets

from api.medication.models import MedicationSchedule, Medication

from api.medication.serializer import MedicationScheduleSerializer, MedicationSerializer


class MedicationScheduleViewSet(viewsets.ModelViewSet):
    queryset = MedicationSchedule.objects.all()
    serializer_class = MedicationScheduleSerializer


class MedicationViewSet(viewsets.ModelViewSet):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer
