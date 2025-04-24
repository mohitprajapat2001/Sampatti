from cities_light.models import City
from banking.constants import AccountType
from cards.constants import CardTypes
from transactions.constants import TransactionTypes
from users.choices import (
    AddressType,
    AccountStatus,
    MarritialStatus,
    GenderChoices,
    QuestionChoices,
    RelationshipChoices,
)
from rest_framework import mixins, viewsets, serializers
from rest_framework.response import Response
from http import HTTPStatus


class CitySerializer(serializers.ModelSerializer):
    """
    Serializer for the City model.
    """

    class Meta:
        model = City
        fields = (
            "id",
            "display_name",
            "name_ascii",
            "country__display_name",
            "region__display_name",
            "latitude",
            "longitude",
        )


class CityListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    API endpoint that allows cities to be viewed.
    """

    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = []

    def filter_queryset(self, queryset):
        filter_queryset = super().filter_queryset(queryset)
        if search := self.request.query_params.get("q"):
            filter_queryset = filter_queryset.filter(name_ascii__icontains=search)
        return filter_queryset


class StaticBaseApi(mixins.ListModelMixin, viewsets.GenericViewSet):
    choice_name = None
    serializer_class = None
    permission_classes = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if not self.choice_name:
            raise ValueError("choice_name must be set")

    def get_queryset(self):
        return [
            {"value": key, "text": value} for key, value in self.choice_name.CHOICES
        ]

    def list(self, request, *args, **kwargs):
        return Response(self.get_queryset(), status=HTTPStatus.OK)


class AccountTypeListViewSet(StaticBaseApi):
    """
    API endpoint that allows account types to be viewed.
    """

    choice_name = AccountType


class CardTypeListViewSet(StaticBaseApi):
    """
    API endpoint that allows card types to be viewed.
    """

    choice_name = CardTypes


class TransactionTypeListViewSet(StaticBaseApi):
    """
    API endpoint that allows transaction types to be viewed.
    """

    choice_name = TransactionTypes


class AddressTypeListViewSet(StaticBaseApi):
    """
    API endpoint that allows address types to be viewed.
    """

    choice_name = AddressType


class MarritialStatusListViewSet(StaticBaseApi):
    """
    API endpoint that allows marital status to be viewed.
    """

    choice_name = MarritialStatus


class GenderChoicesListViewSet(StaticBaseApi):
    """
    API endpoint that allows
    """

    choice_name = GenderChoices


class QuestionChoicesListViewSet(StaticBaseApi):
    """
    API endpoint that allows question choices to be viewed.
    """

    choice_name = QuestionChoices


class RelationshipChoicesListViewSet(StaticBaseApi):
    """
    API endpoint that allows relationship choices to be viewed.
    """

    choice_name = RelationshipChoices


class AccountStatusListViewSet(StaticBaseApi):
    """
    API endpoint that allows account status to be viewed.
    """

    choice_name = AccountStatus
