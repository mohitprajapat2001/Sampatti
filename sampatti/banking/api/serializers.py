from utils.utils import get_model
from utils.constants import AppModel
from banking.constants import ValidationErrors
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
            "city",
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
            "city": {
                "read_only": True,
            },
        }

    def validate(self, attrs):
        attrs = super().validate(attrs)
        if not self.initial_data.get("bank_id"):
            raise serializers.ValidationError(ValidationErrors.BANK_ID_REQUIRED)
        if not Bank.objects.filter(pk=self.initial_data.get("bank_id")).exists():
            raise serializers.ValidationError(ValidationErrors.BANK_NOT_FOUND)
        attrs["bank_id"] = self.initial_data.get("bank_id")
        attrs["city_id"] = 1
        return attrs


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

    def validate(self, attrs):
        attrs = super().validate(attrs)
        if not self.initial_data.get("branch_id"):
            raise serializers.ValidationError(ValidationErrors.BRANCH_ID_REQUIRED)
        if not Branch.objects.filter(pk=self.initial_data.get("branch_id")).exists():
            raise serializers.ValidationError(ValidationErrors.BRANCH_NOT_FOUND)
        attrs["branch_id"] = self.initial_data.get("branch_id")
        attrs["user_id"] = self.initial_data.get("user_id")
        return attrs
