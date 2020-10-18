from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from api.pet.viewsets import (
    SpecieViewSet,
    BreedViewSet,
    PetViewSet
)

from api.medication.viewsets import (
    MedicationScheduleViewSet,
    MedicationViewSet
)

from api.vaccine.viewsets import (
    VaccineViewSet,
    VaccineScheduleViewSet
)

router = routers.DefaultRouter()

router.register('specie', SpecieViewSet, basename='Specie')
router.register('breed', BreedViewSet, basename='Breed')
router.register('pet', PetViewSet, basename='Pet')

router.register('medication_schedule', MedicationScheduleViewSet, basename='Medication Schedule')
router.register('medication', MedicationViewSet, basename='Medication')

router.register('vaccine', VaccineViewSet, basename='Vaccine')
router.register('vaccine_schedule', VaccineScheduleViewSet, basename='Vaccine Schedule')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
