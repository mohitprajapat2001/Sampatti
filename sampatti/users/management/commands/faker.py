from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from faker import Faker
from transactions.constants import TransactionTypes
from utils.utils import get_model
from utils.constants import ManagementConstants, AppModel
from cities_light.models import City
from random import choice
from cards.constants import CardTypes

User = get_user_model()
Bank = get_model(**AppModel.BANK)
Branch = get_model(**AppModel.BRANCH)
Account = get_model(**AppModel.ACCOUNT)
Card = get_model(**AppModel.CARD)
GiftCard = get_model(**AppModel.GIFTCARD)
Transaction = get_model(**AppModel.TRANSACTION)

fake = Faker()


class Command(BaseCommand):
    help = "fake initial data for testing"
    cities = City.objects.all()

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING(ManagementConstants.FAKER_WARNING))
        self.stdout.write(self.style.SUCCESS(ManagementConstants.CREATING_FAKE_USERS))
        bank = Bank.objects.create(title=fake.company())

        self.stdout.write(
            self.style.SUCCESS(ManagementConstants.CREATING_FAKE_BRANCHES), ending=""
        )
        for _ in range(10):
            Branch.objects.create(
                bank=bank, city=choice(self.cities), address=fake.address()
            )
        self.stdout.write(self.style.SUCCESS(ManagementConstants.DOT))
        self.stdout.write(self.style.SUCCESS(ManagementConstants.CREATING_FAKE_USERS))
        for count in range(100):
            email = fake.email()
            while User.objects.filter(email=email).exists():
                email = fake.email()
            user = User.objects.create(
                email=email,
                first_name=fake.first_name(),
                last_name=fake.last_name(),
            )
            account = Account.objects.create(
                user=user, branch=choice(Branch.objects.all())
            )
            Card.objects.create(
                user=user,
                account=account,
                card_type=CardTypes.DEBIT,
                cardholder_name=fake.name(),
            )
            GiftCard.objects.create(
                user=user,
            )
            for _ in range(25):
                Transaction.objects.create(
                    user=user,
                    account=account,
                    transaction_type=choice(TransactionTypes.CHOICES)[0],
                    amount=fake.random_int(min=10, max=1000),
                    description=fake.sentence(),
                )
            self.stdout.write(
                self.style.SUCCESS(ManagementConstants.FAKER_DATA_CREATED % count)
            )
