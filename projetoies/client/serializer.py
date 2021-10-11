from rest_framework.serializers import ModelSerializer

from .models import Client, ClientProfile


class ClientProfileSerializer(ModelSerializer):
    class Meta:
        model = ClientProfile
        fields = "__all__"


class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"
