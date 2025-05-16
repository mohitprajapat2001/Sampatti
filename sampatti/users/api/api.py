from rest_framework import viewsets, generics
from users.api.serializers import (
    UserAverageTransactionSerializer,
    UserExpenseReportSerializer,
    UserSerializer,
    UserDetailSerializer,
    AddressSerializer,
    ProfileSerializer,
    EmergencyDetailsSerializer,
    SecurityQuestionSerializer,
)
from utils.utils import get_model
from utils.constants import AppModel
from rest_framework.decorators import action
from rest_framework.response import Response
from http import HTTPStatus

User = get_model(**AppModel.USER)
UserDetail = get_model(**AppModel.USER_DETAIL)
Profile = get_model(**AppModel.PROFILE)
Address = get_model(**AppModel.ADDRESS)
EmergencyDetails = get_model(**AppModel.EMERGENCY_DETAILS)
SecurityQuestion = get_model(**AppModel.SECURITY_QUESTION)


class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = ()


class UserViewSet(generics.RetrieveUpdateDestroyAPIView, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(methods=["GET"], detail=False)
    def me(self, request, *args, **kwargs):
        """
        action decorator to return authenticated user data
        """
        try:
            serializer = UserDetailSerializer(self.request.user.detail)
        except UserDetail.DoesNotExist:
            serializer = UserDetailSerializer(
                UserDetail.objects.create(user=self.request.user)
            )
        return Response(serializer.data, status=HTTPStatus.OK)

    @action(methods=["GET"], detail=True)
    def transaction_average(self, request, *args, **kwargs):
        """
        Retrieves the average transactions for the specified user.

        This API endpoint returns the average credit, debit, and transfer
        transactions for the user identified by the provided primary key
        in the URL. The data is serialized using the BaseUserSerializer
        and returned in the response.
        """

        user = self.get_object()
        serializer = UserAverageTransactionSerializer(user)
        return Response(serializer.data, status=HTTPStatus.OK)

    @action(methods=["GET"], detail=True)
    def expense_report(self, request, *args, **kwargs):
        """
        Provides an expense report for the specified user.

        This API endpoint returns an expense report for the user identified by
        the provided primary key in the URL. The report includes details about
        the user's spending patterns, categorized expenses, and other relevant
        financial metrics. The data is serialized and returned in the response.
        """
        user = self.get_object()
        serializer = UserExpenseReportSerializer(user)
        return Response(serializer.data, status=HTTPStatus.OK)


class UserDetailViewSet(generics.RetrieveUpdateDestroyAPIView, viewsets.GenericViewSet):
    queryset = UserDetail.objects.all()
    serializer_class = UserDetailSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class EmergencyDetailsViewSet(viewsets.ModelViewSet):
    queryset = EmergencyDetails.objects.all()
    serializer_class = EmergencyDetailsSerializer


class SecurityQuestionViewSet(viewsets.ModelViewSet):
    queryset = SecurityQuestion.objects.all()
    serializer_class = SecurityQuestionSerializer
