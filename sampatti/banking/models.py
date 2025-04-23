from django_extensions.db.models import (
    TimeStampedModel,
    TitleDescriptionModel,
    ActivatorModel,
)
from django.db import models
from cities_light.models import City


class Bank(TimeStampedModel, TitleDescriptionModel, ActivatorModel):
    """
    Model representing a bank.
    """

    def __str__(self):
        return self.title


class Branch(TimeStampedModel, TitleDescriptionModel, ActivatorModel):
    """
    Model representing a bank branch.
    """

    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name="branches")
    branch = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        related_name="branches",
        verbose_name="Branch",
    )
    address = models.TextField(verbose_name="Address", blank=True, null=True)
    code = models.CharField(null=True, blank=True, verbose_name="Branch Code")
    ifsc = models.CharField(
        unique=True, max_length=10, null=True, blank=True, verbose_name="IFSC Code"
    )

    def __str__(self):
        return f"{self.title} - {self.bank.title}"
