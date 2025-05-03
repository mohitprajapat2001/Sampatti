from django.db.models.signals import post_save
from django.dispatch import receiver
from utils.utils import get_model
from utils.constants import AppModel

User = get_model(**AppModel.USER)
UserDetail = get_model(**AppModel.USER_DETAIL)
EMAIL_BASED_USERNAME_EXIST = "%s%s"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Signal to create a user profile when a new user is created.
    """
    if created:
        UserDetail.objects.create(user=instance)
        email = instance.email.split("@")[0]
        instance.username = EMAIL_BASED_USERNAME_EXIST % (
            email,
            instance.id,
        )
        instance.save(update_fields=["username"])
