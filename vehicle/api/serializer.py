from rest_framework import serializers
from .. import models

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vehicle
        # Dados da API
        fields = '__all__'


    
