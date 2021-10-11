from rest_framework.routers import SimpleRouter
from .views import InsuranceCompanyModelViewSet

router = SimpleRouter()

router.register("companies", InsuranceCompanyModelViewSet)
