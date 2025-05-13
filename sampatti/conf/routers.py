from rest_framework.routers import DefaultRouter
from users.api.api import (
    UserViewSet,
    UserDetailViewSet,
    AddressViewSet,
    ProfileViewSet,
    EmergencyDetailsViewSet,
    SecurityQuestionViewSet,
)
from cards.api.api import CardViewSet, GiftCardViewSet
from banking.api.api import BankViewSet, BranchViewSet, AccountViewSet
from transactions.api.api import TransactionsViewSet
from conf.api.api import (
    CityListViewSet,
    CardTypeListViewSet,
    AccountTypeListViewSet,
    AddressTypeListViewSet,
    AccountStatusListViewSet,
    GenderChoicesListViewSet,
    MarritialStatusListViewSet,
    QuestionChoicesListViewSet,
    TransactionTypeListViewSet,
    RelationshipChoicesListViewSet,
)

router = DefaultRouter()

# Default Router for API

router.register("cities", CityListViewSet)
router.register("cardtypes", CardTypeListViewSet, basename="cardtypes")
router.register("accounttypes", AccountTypeListViewSet, basename="accounttypes")
router.register("addresstypes", AddressTypeListViewSet, basename="addresstypes")
router.register("accountstatus", AccountStatusListViewSet, basename="accountstatus")
router.register("genders", GenderChoicesListViewSet, basename="genders")
router.register(
    "marritialstatus", MarritialStatusListViewSet, basename="marritialstatus"
)
router.register("questions", QuestionChoicesListViewSet, basename="questions")
router.register(
    "transactiontypes", TransactionTypeListViewSet, basename="transactiontypes"
)
router.register("relationship", RelationshipChoicesListViewSet, basename="relationship")

# Users App Api Registery
router.register("users", UserViewSet)
router.register("details", UserDetailViewSet)
router.register("profile", ProfileViewSet)
router.register("address", AddressViewSet)
router.register("emerygency", EmergencyDetailsViewSet)
router.register("security", SecurityQuestionViewSet)

# Cards App Api Registery
router.register("cards", CardViewSet)
router.register("giftcards", GiftCardViewSet)


# Banking App Api Registery
router.register("banks", BankViewSet)
router.register("branches", BranchViewSet)
router.register("accounts", AccountViewSet)

# Transactions App Api Registery
router.register("transactions", TransactionsViewSet)
