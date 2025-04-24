from rest_framework import viewsets, generics
from users.api.serializers import (
    UserSerializer,
    UserDetailSerializer,
    AddressSerializer,
    ProfileSerializer,
    EmergencyDetailsSerializer,
    SecurityQuestionSerializer,
)
from utils.utils import get_model
from utils.constants import AppModel

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
