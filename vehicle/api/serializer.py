from rest_framework import serializers
from vehicle.models import Vehicle

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        # Dados da API
        fields = '__all__'


    
