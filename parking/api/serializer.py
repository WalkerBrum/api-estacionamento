from rest_framework import serializers
from .. import models

class ParkingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Parking
        # Dados da API
        fields = '__all__'