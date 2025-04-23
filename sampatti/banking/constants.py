from django.utils.translation import gettext_lazy as _


class AccountType:
    """
    Account types for the bank.
    """

    SAVINGS = "SAVINGS"
    CURRENT = "CURRENT"
    FIXED = "FIXED"
    RECURRING = "RECURRING"

    CHOICES = [
        (SAVINGS, _("Savings")),
        (CURRENT, _("Current")),
        (FIXED, _("Fixed")),
        (RECURRING, _("Recurring")),
    ]
