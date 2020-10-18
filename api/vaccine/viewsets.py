from rest_framework import viewsets

from api.vaccine.models import Vaccine, VaccineSchedule

from api.vaccine.serializer import VaccineSerializer, VaccineScheduleSerializer


class VaccineViewSet(viewsets.ModelViewSet):
    queryset = Vaccine.objects.all()
    serializer_class = VaccineSerializer


class VaccineScheduleViewSet(viewsets.ModelViewSet):
    queryset = VaccineSchedule.objects.all()
    serializer_class = VaccineScheduleSerializer
