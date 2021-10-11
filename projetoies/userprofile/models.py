from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Role(models.Model):
    description = models.CharField(max_length=255)


class UserProfile(models.Model):
    class Status(models.TextChoices):
        ACTIVE = "ACTIVE"
        PENDING = "PENDING"
        FIRED = "FIRED"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField()
    status = models.CharField(choices=Status.choices, max_length=255)
