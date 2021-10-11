from django.db import models
from django.contrib.auth import get_user_model
from client.models import Client
from services.models import Service

User = get_user_model()


class Quote(models.Model):
    class Status(models.TextChoices):
        ACCEPTED = "ACCEPTED"
        PENDING = "PENDING"
        REJECTED = "REJECTED"
        APPROVED_BY_INSURANCE = "APPROVED_BY_INSURANCE"

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    status = models.CharField(choices=Status.choices, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class QuoteDetails(models.Model):
    class Status(models.TextChoices):
        ACTIVE = "ACTIVE"
        NOT_ACTIVE = "NOT_ACTIVE"

    quote = models.ForeignKey(Quote, on_delete=models.CASCADE)
    police_date = models.CharField(max_length=255)
    bank_name = models.CharField(max_length=255)
    bank_number = models.CharField(max_length=255)
    valid_since = models.CharField(max_length=255)
    valid_until = models.CharField(max_length=255)
    police_amount = models.CharField(max_length=255)
    status = models.CharField(choices=Status.choices, max_length=255)
