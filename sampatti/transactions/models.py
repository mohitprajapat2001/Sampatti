from django_extensions.db.models import TimeStampedModel
from django.db import models
from banking.models import Account
from transactions.constants import TransactionTypes


class Transaction(TimeStampedModel):

    account = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name="transactions"
    )
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="transactions"
    )
    transaction_type = models.CharField(max_length=3, choices=TransactionTypes.CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.transaction_type} - {self.amount} - {self.account}"
