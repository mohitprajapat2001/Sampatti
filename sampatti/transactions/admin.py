from django.contrib.admin import ModelAdmin, register
from utils.utils import get_model
from utils.constants import AppModel
from admin_auto_filters.filters import AutocompleteFilter

Transaction = get_model(**AppModel.TRANSACTION)


class UserFilter(AutocompleteFilter):
    title = "User"
    field_name = "user"


@register(Transaction)
class TransactionAdmin(ModelAdmin):
    list_filter = (UserFilter, "account__account_type", "created")
    search_fields = (
        "description",
        "account__account_number",
        "user__email",
        "account__account_type",
    )
