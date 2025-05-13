from utils.utils import get_model
from utils.constants import AppModel
from rest_framework import serializers
from users.api.serializers import UserSerializer
from banking.api.serializers import AccountSerializer

Transaction = get_model(**AppModel.TRANSACTION)


class TransactionSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    account = AccountSerializer(read_only=True)

    class Meta:
        model = Transaction
        fields = (
            "id",
            "user",
            "account",
            "transaction_type",
            "amount",
            "description",
            "created",
            "modified",
        )
