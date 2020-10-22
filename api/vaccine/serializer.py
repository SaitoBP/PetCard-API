from rest_framework import serializers

from api.vaccine.models import Vaccine, VaccineSchedule


class VaccineSerializer(serializers.ModelSerializer):

    vaccine_schedule = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='Vaccine Schedule-detail'
    )

    class Meta:
        model = Vaccine
        fields = ['id', 'vaccine', 'description', 'vaccine_schedule']


class VaccineScheduleSerializer(serializers.ModelSerializer):

    status = serializers.BooleanField(source='validate_status')

    class Meta:
        model = VaccineSchedule
        fields = ['id', 'vaccine', 'schedule', 'cycle', 'status']
