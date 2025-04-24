from utils.utils import get_model
from utils.constants import AppModel
from users.api.serializers import UserSerializer
from banking.api.serializers import AccountSerializer
from utils.serializers import CustomForeignKeySerializer

Card = get_model(**AppModel.CARD)
GiftCard = get_model(**AppModel.GIFTCARD)


class CardSerializer(CustomForeignKeySerializer):
    user = UserSerializer(read_only=True)
    account = AccountSerializer(read_only=True)

    class Meta:
        model = Card
        fields = (
            "id",
            "user",
            "account",
            "card_number",
            "card_type",
            "cardholder_name",
            "expiry_date",
            "cvv",
        )
        extra_kwargs = {
            "card_number": {"read_only": True},
        }


class GiftCardSerializer(CustomForeignKeySerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = GiftCard
        fields = (
            "id",
            "user",
            "card_number",
            "balance",
            "expiry_date",
        )
        extra_kwargs = {
            "card_number": {"read_only": True},
        }
