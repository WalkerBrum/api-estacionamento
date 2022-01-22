from rest_framework import viewsets
from user import models
from user.api.serizalizer import UserSerializer
from rest_framework.permissions import IsAuthenticated


# Class para fazer API funcionar
class UserViewSet(viewsets.ModelViewSet):
    # Asking authentication for acess
    permission_classes = (IsAuthenticated,)

    queryset = models.User.objects.all()
    serializer_class = UserSerializer