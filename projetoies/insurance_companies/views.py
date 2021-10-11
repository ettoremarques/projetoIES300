from rest_framework.viewsets import ModelViewSet
from .models import InsuranceCompany
from .serializer import InsuranceCompanySerializer


class InsuranceCompanyModelViewSet(ModelViewSet):
    queryset = InsuranceCompany.objects.all()
    serializer_class = InsuranceCompanySerializer
