from rest_framework import serializers

from api.medication.models import MedicationSchedule, Medication


class MedicationScheduleSerializer(serializers.ModelSerializer):
    status = serializers.BooleanField(source='validate_status')

    class Meta:
        model = MedicationSchedule
        fields = ['medication', 'schedule', 'cycle', 'status']


class MedicationSerializer(serializers.ModelSerializer):
    medication_schedule = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='Medication Schedule-detail'
    )

    class Meta:
        model = Medication
        fields = ['id', 'medicine', 'description', 'medication_schedule']
