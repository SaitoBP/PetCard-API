from rest_framework import serializers

from api.pet.models import (
    Specie,
    Pet,
    Breed
)


class SpecieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specie
        fields = "__all__"


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = "__all__"


class PetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pet
        fields = "__all__"

