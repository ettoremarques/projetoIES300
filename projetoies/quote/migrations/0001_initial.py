# Generated by Django 3.2.8 on 2021-10-11 01:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("client", "0001_initial"),
        ("services", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Quote",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("ACCEPTED", "Accepted"),
                            ("PENDING", "Pending"),
                            ("REJECTED", "Rejected"),
                            ("APPROVED_BY_INSURANCE", "Approved By Insurance"),
                        ],
                        max_length=255,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "client",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="client.client"
                    ),
                ),
                (
                    "service",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="services.service",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="QuoteDetails",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("police_date", models.CharField(max_length=255)),
                ("bank_name", models.CharField(max_length=255)),
                ("bank_number", models.CharField(max_length=255)),
                ("valid_since", models.CharField(max_length=255)),
                ("valid_until", models.CharField(max_length=255)),
                ("police_amount", models.CharField(max_length=255)),
                (
                    "status",
                    models.CharField(
                        choices=[("ACTIVE", "Active"), ("NOT_ACTIVE", "Not Active")],
                        max_length=255,
                    ),
                ),
                (
                    "quote",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="quote.quote"
                    ),
                ),
            ],
        ),
    ]