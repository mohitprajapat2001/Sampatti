from utils.utils import get_model
from utils.constants import AppModel
from rest_framework import serializers
from users.api.serializers import UserSerializer

Bank = get_model(**AppModel.BANK)
Branch = get_model(**AppModel.BRANCH)
Account = get_model(**AppModel.ACCOUNT)


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = (
            "id",
            "title",
            "description",
            "created",
            "modified",
            "status",
        )


class BranchSerializer(serializers.ModelSerializer):
    bank = BankSerializer(read_only=True)

    class Meta:
        model = Branch
        fields = (
            "id",
            "bank",
            "address",
            "code",
            "ifsc",
            "created",
            "modified",
            "status",
        )
        extra_kwargs = {
            "code": {
                "read_only": True,
            },
            "ifsc": {
                "read_only": True,
            },
        }


class AccountSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    branch = BranchSerializer(read_only=True)

    class Meta:
        model = Account
        fields = (
            "id",
            "user",
            "branch",
            "account_type",
            "account_number",
            "balance",
        )
        extra_kwargs = {
            "account_number": {
                "read_only": True,
            },
            "balance": {
                "read_only": True,
            },
        }
