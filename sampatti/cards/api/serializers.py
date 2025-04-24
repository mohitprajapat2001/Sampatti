from utils.utils import get_model
from utils.constants import AppModel
from rest_framework import serializers
from users.api.serializers import UserSerializer

Card = get_model(**AppModel.CARD)
GiftCard = get_model(**AppModel.GIFTCARD)


class CardSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    # TODO: Add account related serializer
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
            "pin",
        )
        extra_kwargs = {
            "card_number": {"read_only": True},
        }


class GiftCardSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    # TODO: Add account related serializer
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
