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

router = routers.DefaultRouter()
router.register('specie', SpecieViewSet, basename='Specie')
router.register('breed', BreedViewSet, basename='Breed')
router.register('pet', PetViewSet, basename='Pet')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
