from django.contrib import admin
from utils.utils import get_model
from utils.constants import AppModel

User = get_model(**AppModel.USER)
UserDetail = get_model(**AppModel.USER_DETAIL)
UserProfile = get_model(**AppModel.PROFILE)
UserAddress = get_model(**AppModel.ADDRESS)
UserEmergencyDetails = get_model(**AppModel.EMERGENCY_DETAILS)
UserSecurityQuestion = get_model(**AppModel.SECURITY_QUESTION)


class UserDetailInline(admin.StackedInline):
    model = UserDetail
    extra = 0


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    extra = 0
    min_num = 1


class UserAddressInline(admin.StackedInline):
    model = UserAddress
    extra = 0


class UserEmergencyDetailsInline(admin.StackedInline):
    model = UserEmergencyDetails
    extra = 0


class UserSecurityQuestionInline(admin.StackedInline):
    model = UserSecurityQuestion
    extra = 0


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    Admin view for the User model.
    """

    list_display = (
        "username",
        "email",
        "phone_number",
        "status",
        "is_active",
        "is_staff",
        "is_superuser",
    )
    search_fields = ("username", "email", "phone_number")
    list_filter = ("status",)
    ordering = ("-date_joined",)
    inlines = [
        UserDetailInline,
        UserProfileInline,
        UserAddressInline,
        UserEmergencyDetailsInline,
        UserSecurityQuestionInline,
    ]
