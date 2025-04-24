from utils.utils import get_model
from utils.constants import AppModel
from rest_framework import serializers
from users.api.serializers import UserSerializer

Transaction = get_model(**AppModel.TRANSACTION)


class TransactionSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    # TODO: Add Account Serializers and update here
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
