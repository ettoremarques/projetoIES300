from rest_framework.serializers import ModelSerializer
from .models import Quote, QuoteDetails


class QuoteSerializer(ModelSerializer):
    class Meta:
        model = Quote
        fields = "__all__"


class QuoteDetailsSerializer(ModelSerializer):
    class Meta:
        model = QuoteDetails
        fields = "__all__"
