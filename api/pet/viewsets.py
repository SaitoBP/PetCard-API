from rest_framework import viewsets

from api.pet.models import (
    Specie,
    Breed,
    Pet

)

from api.pet.serializer import (
    SpecieSerializer,
    BreedSerializer,
    PetSerializer
)


class SpecieViewSet(viewsets.ModelViewSet):
    """
    Simple ViewSet for Pet Species
    """

    queryset = Specie.objects.all()
    serializer_class = SpecieSerializer


class BreedViewSet(viewsets.ModelViewSet):
    """
    Simple ViewSet for Pet Breed
    """

    queryset = Breed.objects.all()
    serializer_class = BreedSerializer


class PetViewSet(viewsets.ModelViewSet):
    """
    Simple ViewSet for Pets
    """

    queryset = Pet.objects.all()
    serializer_class = PetSerializer
