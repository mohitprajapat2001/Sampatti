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
router.register("cardtypes", CardTypeListViewSet)
router.register("accounttypes", AccountTypeListViewSet)
router.register("addresstypes", AddressTypeListViewSet)
router.register("accountstatus", AccountStatusListViewSet)
router.register("genders", GenderChoicesListViewSet)
router.register("marritialstatus", MarritialStatusListViewSet)
router.register("questions", QuestionChoicesListViewSet)
router.register("transactiontypes", TransactionTypeListViewSet)
router.register("relationship", RelationshipChoicesListViewSet)

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
