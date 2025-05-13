from rest_framework.viewsets import ModelViewSet
from transactions.api.serializers import TransactionSerializer
from utils.utils import get_model
from utils.constants import AppModel
from transactions.filter import TransactionFilter

Transaction = get_model(**AppModel.TRANSACTION)


class TransactionsViewSet(ModelViewSet):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()
    ordering = ("-created",)
    filterset_class = TransactionFilter
