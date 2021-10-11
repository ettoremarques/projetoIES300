from rest_framework.routers import SimpleRouter
from .views import QuoteModelViewSet, QuoteDetailsModelViewSet

router = SimpleRouter()

router.register("quote", QuoteModelViewSet)
router.register("quote_details", QuoteDetailsModelViewSet)
