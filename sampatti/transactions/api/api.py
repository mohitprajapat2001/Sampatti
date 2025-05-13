from rest_framework.viewsets import ModelViewSet
from transactions.api.serializers import TransactionSerializer
from utils.utils import get_model
from utils.constants import AppModel
from django.db.models import Q

Transaction = get_model(**AppModel.TRANSACTION)


class TransactionsViewSet(ModelViewSet):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()
    ordering = ("-created",)

    def get_queryset(self):
        qs = super().get_queryset().filter(user=self.request.user)
        query = Q()
        if search := self.request.query_params.get("q"):
            query |= Q(description__icontains=search)
        return qs.filter(query)
