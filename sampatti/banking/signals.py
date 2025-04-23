from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save
from utils.utils import get_model
from utils.constants import AppModel


Branch = get_model(**AppModel.BRANCH)


@receiver(post_save, sender=Branch)
def branch_post_save(sender, instance, created, **kwargs):
    """
    Signal to update the Branch IFSC code after saving the Branch instance.
    :param sender: The model class that sent the signal.
    :param instance: The actual instance being saved.
    :param created: Boolean; True if a new record was created.
    constraint: The signal is sent after the instance is saved.
    1. length of IFSC code should be 10 characters.
    2. IFSC code should be unique.
    3. IFSC code's first four characters should be alphabets.
    4. IFSC code's last six characters should be digits.
    5. IFSC code should not be empty.
    """

    if created:
        instance.code = str(instance.pk).zfill(6)
        instance.ifsc = instance.bank.title[:4].upper() + str(instance.pk).zfill(6)
        instance.save(update_fields=["ifsc", "code"])
