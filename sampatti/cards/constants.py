from django.utils.translation import gettext_lazy as _


class CardTypes:
    """
    Card types for the banking application.
    """

    DEBIT = "debit"
    CREDIT = "credit"
    PREPAID = "prepaid"

    CHOICES = [
        (DEBIT, _("Debit")),
        (CREDIT, _("Credit")),
    ]
