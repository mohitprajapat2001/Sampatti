from django_extensions.db.models import (
    TimeStampedModel,
    TitleDescriptionModel,
    ActivatorModel,
)
from django.db import models
from cities_light.models import City
from banking.constants import AccountType


class Bank(TimeStampedModel, TitleDescriptionModel, ActivatorModel):
    """
    Model representing a bank.
    """

    def __str__(self):
        return self.title


class Branch(TimeStampedModel, ActivatorModel):
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
    code = models.CharField(
        max_length=4, null=True, blank=True, verbose_name="Branch Code"
    )
    ifsc = models.CharField(
        unique=True, max_length=10, null=True, blank=True, verbose_name="IFSC Code"
    )

    def __str__(self):
        return f"{self.bank.title}"


class Account(TimeStampedModel, ActivatorModel):
    """
    Model representing a bank account.
    """

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="accounts"
    )
    branch = models.ForeignKey(
        "banking.Branch", on_delete=models.CASCADE, related_name="accounts"
    )
    account_type = models.CharField(
        max_length=10, choices=AccountType.CHOICES, default=AccountType.SAVINGS
    )
    account_number = models.CharField(max_length=10, unique=True, null=True, blank=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.user.username} - {self.account_number}"
