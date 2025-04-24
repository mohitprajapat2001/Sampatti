from rest_framework.routers import DefaultRouter
from users.api.api import (
    UserViewSet,
    UserDetailViewSet,
    AddressViewSet,
    ProfileViewSet,
    EmergencyDetailsViewSet,
    SecurityQuestionViewSet,
)

router = DefaultRouter()

# Users App Api Registery
router.register("users", UserViewSet)
router.register("details", UserDetailViewSet)
router.register("profile", ProfileViewSet)
router.register("address", AddressViewSet)
router.register("emerygency", EmergencyDetailsViewSet)
router.register("security", SecurityQuestionViewSet)
