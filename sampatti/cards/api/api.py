from utils.utils import get_model
from utils.constants import AppModel
from rest_framework import viewsets
from cards.api.serializers import CardSerializer, GiftCardSerializer

Card = get_model(**AppModel.CARD)
GiftCard = get_model(**AppModel.GIFTCARD)


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class GiftCardViewSet(viewsets.ModelViewSet):
    queryset = GiftCard.objects.all()
    serializer_class = GiftCardSerializer
