from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save
from utils.utils import get_model
from utils.constants import AppModel
import random
from django.utils.timezone import now, timedelta

Card = get_model(**AppModel.CARD)


@receiver(post_save, sender=Card)
def card_post_save(sender, instance, created, **kwargs):
    """
    Signal to update the Card number after saving the Card instance.
    :param sender: The model class that sent the signal.
    :param instance: The actual instance being saved.
    :param created: Boolean; True if a new record was created.
    constraint: The signal is sent after the instance is saved.
    1. length of Card number should be 16 characters.
    2. Card number should be unique.
    3. Card number should not be empty.
    - Card Expiry date should be in the format MM/YYYY.
    - Card CVV should be in the format 3 digits.
    1. Expiry date should be in the future.
    2. Expiry date should not be empty.
    3. CVV should be in the format 3 digits.
    4. CVV should not be empty.
    """
    if created:
        value = "".join([str(random.randint(0, 9)) for _ in range(16)])
        while not Card.objects.filter(card_number=value).exists():
            instance.card_number = "".join(
                [str(random.randint(0, 9)) for _ in range(16)]
            )
            break
        if not instance.cardholder_name:
            instance.cardholder_name = (
                instance.user.get_full_name().title() or instance.user.username.title()
            )
        instance._expiry_date = now() + timedelta(days=(365 * 5 + 1))
        instance._cvv = "".join([str(random.randint(0, 9)) for _ in range(3)])
        instance.save(update_fields=["card_number", "_expiry_date", "_cvv"])
