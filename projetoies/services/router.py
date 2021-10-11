from rest_framework.routers import SimpleRouter
from .views import ServiceModelViewSet

router = SimpleRouter()

router.register("service", ServiceModelViewSet)
