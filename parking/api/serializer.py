from rest_framework import serializers
from parking.models import Parking

class ParkingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parking
        # Dados da API
        fields = '__all__'