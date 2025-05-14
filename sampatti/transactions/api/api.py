from rest_framework.viewsets import ModelViewSet
from transactions.api.serializers import TransactionSerializer
from utils.utils import get_model
from utils.constants import AppModel
from transactions.filter import TransactionFilter
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated

Transaction = get_model(**AppModel.TRANSACTION)


class TransactionsViewSet(ModelViewSet):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()
    ordering = ("-created",)
    filterset_class = TransactionFilter
    permission_classes = (DjangoModelPermissions, IsAuthenticated)
