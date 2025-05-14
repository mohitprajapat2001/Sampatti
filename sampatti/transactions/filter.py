from django_filters import rest_framework as filters
from utils.utils import get_model
from utils.constants import AppModel

Transaction = get_model(**AppModel.TRANSACTION)


class TransactionFilter(filters.FilterSet):
    """
    Transaction model Filter
    """

    q = filters.CharFilter(field_name="description", lookup_expr="icontains")
    account = filters.NumberFilter(
        field_name="account__account_anumber", lookup_expr="contains"
    )
    user = filters.NumberFilter(field_name="user__id", lookup_expr="exact")

    class Meta:
        model = Transaction
        fields = ("account", "user", "transaction_type", "q", "user", "account")
