from django.db import models
from services.models import Service


class InsuranceCompany(models.Model):
    class Status(models.TextChoices):
        OPERATIONAL = "OPERATIONAL"
        NOT_OPERATIONAL = "NOT_OPERATIONAL"

    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    site = models.CharField(max_length=255)
    contact_name = models.CharField(max_length=255)
    contact_email = models.CharField(max_length=255)
    status = models.CharField(choices=Status.choices, max_length=255)
