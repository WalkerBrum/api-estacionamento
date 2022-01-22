from rest_framework import viewsets
from parking import models
from parking.api.serializer import ParkingSerializer
from rest_framework.permissions import IsAuthenticated

# Class para fazer API funcionar
class ParkingViewSet(viewsets.ModelViewSet):
    # Asking authentication for acess
    permission_classes = (IsAuthenticated,)

    queryset = models.Parking.objects.all()
    serializer_class = ParkingSerializer