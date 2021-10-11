from .models import Service
from .serializer import ServiceSerializer
from rest_framework.viewsets import ModelViewSet


class ServiceModelViewSet(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
