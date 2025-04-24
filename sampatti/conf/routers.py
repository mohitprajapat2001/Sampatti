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

router = DefaultRouter()

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
router.register("bank", BankViewSet)
router.register("branch", BranchViewSet)
router.register("account", AccountViewSet)
