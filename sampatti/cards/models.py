from django.db import models
from django_extensions.db.models import TimeStampedModel, ActivatorModel
from cards.constants import CardTypes
from django.contrib.auth.hashers import make_password, check_password
from django.utils.timezone import now, timedelta


def expiry_date_default():
    """
    Default value for the expiry date of a card.
    """

    return now() + timedelta(days=365 * 5 + 1)


class Card(TimeStampedModel, ActivatorModel):
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="cards"
    )
    account = models.ForeignKey(
        "banking.Account", on_delete=models.CASCADE, related_name="cards"
    )
    card_number = models.CharField(max_length=16, unique=True, null=True, blank=True)
    card_type = models.CharField(max_length=10, choices=CardTypes.CHOICES)
    cardholder_name = models.CharField(max_length=100, null=True, blank=True)
    _expiry_date = models.DateField(null=True, blank=True, db_column="expiry_date")
    _cvv = models.CharField(max_length=3, null=True, blank=True, db_column="cvv")
    _pin = models.CharField(max_length=4, db_column="pin", null=True, blank=True)
    credit_limit = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00, null=True, blank=True
    )

    @property
    def pin(self):
        """
        Get the pin for the card.
        """
        return AttributeError("PIN is only writable.")

    @property
    def expiry_date(self):
        """
        Get the expiry date for the card.
        """
        return self._expiry_date.strftime("%m/%Y")

    @property
    def cvv(self):
        """
        Get the CVV for the card.
        """
        return self._cvv

    @pin.setter
    def pin(self, value):
        """
        Set the pin for the card.
        """
        self._pin = make_password(value)
        self.save(update_fields=["_pin"])

    def check_pin(self, pin):
        """
        Check if the provided pin matches the stored pin.
        """
        return check_password(pin, self._pin)

    def update_pin(self, new_pin):
        """
        Update the pin for the card.
        """
        self._pin = make_password(new_pin)
        self.save(update_fields=["pin"])

    def __str__(self):
        return f"{self.card_type.capitalize()} Card - **** {self.card_number[-4:]}"

    def delete(self, *args, **kwargs):
        """
        Deactivate the card without deleting it.
        """
        self.status = ActivatorModel.INACTIVE_STATUS
        self.save(update_fields=["status"])

    def force_delete(self, *args, **kwargs):
        """
        Force delete the card without any cleanup.
        """
        super().delete(*args, **kwargs)

    def deactivate(self):
        """
        Deactivate the card.
        """
        super().delete()

    def activate(self):
        """
        Activate the card.
        """
        self.status = ActivatorModel.ACTIVE_STATUS
        self.save(update_fields=["status"])

    def save(self, *args, **kwargs):
        """
        Save the card instance.
        """
        if self.card_type == CardTypes.CREDIT:
            if not self.credit_limit:
                raise ValueError("Credit limit is required for credit cards.")
        super().save(*args, **kwargs)


class GiftCard(TimeStampedModel):
    """
    Model representing a gift card.
    """

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="gift_cards"
    )
    card_number = models.CharField(max_length=16, unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    expiry_date = models.DateField(default=expiry_date_default)

    def __str__(self):
        return f"Gift Card - **** {self.card_number[-4:]}"
