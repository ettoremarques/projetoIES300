from .views import UserViewSet, UserProfileViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register("user", UserViewSet)
router.register("user_profile", UserProfileViewSet)
