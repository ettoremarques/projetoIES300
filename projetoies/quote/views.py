from rest_framework.viewsets import ModelViewSet
from .models import Quote, QuoteDetails
from .serializer import QuoteSerializer, QuoteDetailsSerializer


class QuoteModelViewSet(ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer


class QuoteDetailsModelViewSet(ModelViewSet):
    queryset = QuoteDetails.objects.all()
    serializer_class = QuoteDetailsSerializer
