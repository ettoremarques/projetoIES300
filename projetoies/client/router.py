from rest_framework.routers import SimpleRouter
from .views import ClientModelViewSet, ClientProfileModelViewSet


router = SimpleRouter()

router.register("client", ClientModelViewSet)
router.register("client_profile", ClientProfileModelViewSet)
