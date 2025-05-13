from django.utils.translation import gettext_lazy as _


class GroupChoices:
    SUPERUSER = "superuser"
    MANAGER = "manager"
    EMPLOYEE = "employee"
    CUSTOMER = "customer"

    CHOICES = (
        (SUPERUSER, _("Superuser")),
        (MANAGER, _("Manager")),
        (EMPLOYEE, _("Employee")),
        (CUSTOMER, _("Customer")),
    )
