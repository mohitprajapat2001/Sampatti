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


class ValidationErrors:
    BANK_ID_REQUIRED = _("Bank id is required.")
    BANK_NOT_FOUND = _("Bank not found")
    BRANCH_ID_REQUIRED = _("Branch id is required")
    BRANCH_NOT_FOUND = _("Branch Not Found")
    CITY_ID_REQUIRED = _("City id is required")
    CITY_NOT_FOUND = _("City Not Found")
    ACCOUNT_ID_REQUIRED = _("Account id is required")
    ACCOUNT_NOT_FOUND = _("Account Not Found")
