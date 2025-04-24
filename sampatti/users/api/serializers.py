from rest_framework import serializers
from utils.utils import get_model
from utils.constants import AppModel
from django.contrib.auth.password_validation import validate_password
from users.constants import ValidationErrors

User = get_model(**AppModel.USER)
UserDetail = get_model(**AppModel.USER_DETAIL)
Profile = get_model(**AppModel.PROFILE)
Address = get_model(**AppModel.ADDRESS)
EmergencyDetails = get_model(**AppModel.EMERGENCY_DETAILS)
SecurityQuestion = get_model(**AppModel.SECURITY_QUESTION)


class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(
        write_only=True,
        style={"input_type": "password"},
        required=True,
    )

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "status",
            "phone_number",
            "date_joined",
            "password",
            "confirm_password",
        )
        extra_kwargs = {
            "password": {
                "write_only": True,
                "style": {"input_type": "password"},
            },
            "status": {
                "read_only": True,
            },
            "date_joined": {
                "read_only": True,
            },
        }

    def validate_password(self, value):
        """
        Validate the password field.
        """
        validate_password(value)
        return value

    def validate(self, attrs):
        attrs = super().validate(attrs)
        if attrs["password"] != attrs["confirm_password"]:
            raise serializers.ValidationError(
                {"confirm_password": ValidationErrors.PASSWORD_MISMATCH}
            )
        return attrs

    def create(self, validated_data):
        validated_data.pop("confirm_password")
        return super().create(validated_data)


class UserDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer(
        read_only=True,
        default=serializers.CurrentUserDefault(),
    )

    class Meta:
        model = UserDetail
        fields = (
            "id",
            "user",
            "secondary_email",
            "date_of_birth",
            "gender",
            "marrital_status",
            "bio",
            "age",
            "age_nicely",
        )


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = (
            "id",
            "user",
            "image",
            "primary",
        )


class AddressSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Address
        fields = (
            "id",
            "user",
            "address_line_1",
            "address_line_2",
            "city",
            "pincode",
            "address_type",
        )


class EmergencyDetailsSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = EmergencyDetails
        fields = (
            "id",
            "user",
            "name",
            "phone_number",
            "relationship",
        )


class SecurityQuestionSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = SecurityQuestion
        fields = (
            "id",
            "question",
            "answer",
        )
