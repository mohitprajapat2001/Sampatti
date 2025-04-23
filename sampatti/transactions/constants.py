from django.utils.translation import gettext_lazy as _


class TransactionTypes:
    """
    Transaction types for the banking application.
    """

    DEPOSIT = "deposit"
    WITHDRAWAL = "withdrawal"
    TRANSFER = "transfer"
    DEDUCTION = "deduction"
    EMI = "emi"
    INTEREST = "interest"

    CHOICES = [
        (DEPOSIT, _("Deposit")),
        (WITHDRAWAL, _("Withdrawal")),
        (TRANSFER, _("Transfer")),
        (DEDUCTION, _("Deduction")),
        (EMI, _("EMI")),
        (INTEREST, _("Interest")),
    ]
