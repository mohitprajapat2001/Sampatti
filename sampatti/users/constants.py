from django.utils.translation import gettext_lazy as _

USER_PROFILE_UPLOAD_MEDIA_PATH = "user_profile/%s/%s"


class ValidationErrors:
    """
    Users App Validation Errors
    """

    INVALID_CREDENTAILS = _("Email or password is incorrect")
