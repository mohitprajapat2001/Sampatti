from utils.utils import get_model
from utils.constants import AppModel
from rest_framework import viewsets
from banking.api.serializers import BankSerializer, BranchSerializer, AccountSerializer

Bank = get_model(**AppModel.BANK)
Branch = get_model(**AppModel.BRANCH)
Account = get_model(**AppModel.ACCOUNT)


class BankViewSet(viewsets.ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
