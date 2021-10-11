from rest_framework.viewsets import ModelViewSet
from .models import Client, ClientProfile
from .serializer import ClientSerializer, ClientProfileSerializer


class ClientModelViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientProfileModelViewSet(ModelViewSet):
    queryset = ClientProfile.objects.all()
    serializer_class = ClientProfileSerializer
