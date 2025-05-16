from rest_framework import serializers
from utils.utils import get_model
from utils.constants import AppModel
from django.contrib.auth.password_validation import validate_password
from users.constants import ValidationErrors
from utils.serializers import CustomForeignKeySerializer
from django.utils.timezone import now, timedelta
from utils.constants import DD_MM_YYYY

User = get_model(**AppModel.USER)
UserDetail = get_model(**AppModel.USER_DETAIL)
Profile = get_model(**AppModel.PROFILE)
Address = get_model(**AppModel.ADDRESS)
EmergencyDetails = get_model(**AppModel.EMERGENCY_DETAILS)
SecurityQuestion = get_model(**AppModel.SECURITY_QUESTION)


class BaseUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "get_full_name",
            "email",
            "status",
        )


class UserAverageTransactionSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = (
            "id",
            "username",
            "get_full_name",
            "email",
            "status",
            "last_month_average_credit_transactions",
            "last_month_average_debit_transactions",
            "last_month_average_transfer_transactions",
            "this_month_average_credit_transactions",
            "this_month_average_debit_transactions",
            "this_month_average_transfer_transactions",
        )


class UserExpenseReportSerializer(BaseUserSerializer):
    seven_days = serializers.SerializerMethodField()
    one_month = serializers.SerializerMethodField()
    three_month = serializers.SerializerMethodField()

    class Meta(BaseUserSerializer.Meta):
        fields = (
            "id",
            "username",
            "get_full_name",
            "email",
            "status",
            "seven_days",
            "one_month",
            "three_month",
        )

    def get_seven_days(self, obj):
        seven_days_report = {}
        for day in range(0, 7):
            date = now().date() - timedelta(days=day)
            seven_days_report[date.strftime(DD_MM_YYYY)] = obj.expense_report_days(day)
        return seven_days_report

    def get_one_month(self, obj):
        one_month_report = {}
        for day in range(0, 29):
            date = now().date() - timedelta(days=day)
            one_month_report[date.strftime(DD_MM_YYYY)] = obj.expense_report_days(day)
        return one_month_report

    def get_three_month(self, obj):
        three_month_report = {}
        for month in range(0, 3):
            monthh = now().month - month
            year = now().year
            if monthh < 1:
                year = year - 1
                monthh = 12 + monthh
            three_month_report[
                now().strptime(f"01-{monthh}-{year}", DD_MM_YYYY).strftime(DD_MM_YYYY)
            ] = obj.expense_report_month(month)
        return three_month_report


class UserSerializer(BaseUserSerializer):
    confirm_password = serializers.CharField(
        write_only=True,
        style={"input_type": "password"},
        required=True,
    )

    class Meta(BaseUserSerializer.Meta):
        fields = (
            "id",
            "username",
            "get_full_name",
            "first_name",
            "last_name",
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
        user = super().create(validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user


class UserDetailSerializer(CustomForeignKeySerializer):
    user = UserSerializer(read_only=True)

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


class ProfileSerializer(CustomForeignKeySerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = (
            "id",
            "user",
            "image",
            "primary",
        )


class AddressSerializer(CustomForeignKeySerializer):
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


class EmergencyDetailsSerializer(CustomForeignKeySerializer):
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


class SecurityQuestionSerializer(CustomForeignKeySerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = SecurityQuestion
        fields = (
            "id",
            "question",
            "answer",
        )
