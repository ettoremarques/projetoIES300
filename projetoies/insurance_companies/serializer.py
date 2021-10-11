from rest_framework.serializers import ModelSerializer
from .models import InsuranceCompany


class InsuranceCompanySerializer(ModelSerializer):
    class Meta:
        model = InsuranceCompany
        fields = "__all__"
