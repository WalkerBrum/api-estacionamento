from rest_framework import viewsets
from vehicle import models
from vehicle.api.serializer import VehicleSerializer
from rest_framework.permissions import IsAuthenticated


# Class para fazer API funcionar
class DriverViewSet(viewsets.ModelViewSet):
    # Asking authentication for acess
    permission_classes = (IsAuthenticated,)

    queryset = models.Vehicle.objects.all()
    serializer_class = VehicleSerializer
