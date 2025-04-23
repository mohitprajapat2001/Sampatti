from django.db import models
from django_extensions.db.models import TimeStampedModel
from cards.constants import CardTypes


class Card(TimeStampedModel):
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="cards"
    )
    account = models.ForeignKey(
        "banking.Account", on_delete=models.CASCADE, related_name="cards"
    )
    card_number = models.CharField(max_length=16, unique=True, null=True, blank=True)
    card_type = models.CharField(max_length=10, choices=CardTypes.CHOICES)
    cardholder_name = models.CharField(max_length=100)
    expiry_date = models.DateField()
    cvv = models.CharField(max_length=3)
    pin = models.CharField(max_length=4)

    def __str__(self):
        return f"{self.card_type.capitalize()} Card - **** {self.card_number[-4:]}"


class GiftCard(TimeStampedModel):
    """
    Model representing a gift card.
    """

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="gift_cards"
    )
    card_number = models.CharField(max_length=16, unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    expiry_date = models.DateField()

    def __str__(self):
        return f"Gift Card - **** {self.card_number[-4:]}"
