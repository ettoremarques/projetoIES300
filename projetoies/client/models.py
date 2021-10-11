from django.db import models


class Client(models.Model):
    class Status(models.TextChoices):
        ACTIVE = "ACTIVE"
        NOT_ACTIVE = "NOT_ACTIVE"

    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=Status.choices, max_length=255)
    birth_date = models.DateField()
    email = models.EmailField()


class ClientProfile(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    rg = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    marital_status = models.CharField(max_length=255)
    profession = models.CharField(max_length=255)
    sex = models.CharField(max_length=255)
    mothers_name = models.CharField(max_length=255)
    fathers_name = models.CharField(max_length=255)
    observations = models.CharField(max_length=255)
