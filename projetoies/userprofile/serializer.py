from rest_framework.serializers import ModelSerializer
from .models import UserProfile, User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"
