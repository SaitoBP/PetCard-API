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
    pet_medication = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='Medication-detail'
    )

    pet_vaccine = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='Vaccine-detail'
    )

    class Meta:
        model = Pet
        fields = ['id', 'photo', 'name', 'age',
                  'gender', 'weight', 'breed',
                  'pet_medication', 'pet_vaccine']
