from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from users.choices import (
    AddressType,
    MarritialStatus,
    AccountStatus,
    GenderChoices,
    RelationshipChoices,
    QuestionChoices,
)
from users.constants import USER_PROFILE_UPLOAD_MEDIA_PATH
from cities_light.models import City
from django.utils.timezone import now
from django.utils import timesince


def _user_profile_image(self, filename) -> str:
    """
    Generates the path for the user profile image.

    :param self: User Instance
    """
    return USER_PROFILE_UPLOAD_MEDIA_PATH % (self.user.id, filename)


class User(AbstractUser):
    """
    Custom user model that extends the default Django user model.
    """

    email = models.EmailField(unique=True, verbose_name="Email Address")
    phone_number = PhoneNumberField(
        unique=True, null=True, blank=True, verbose_name="Phone Number", region="IN"
    )
    status = models.CharField(
        max_length=255,
        choices=AccountStatus.CHOICES,
        default=AccountStatus.ACTIVE,
        verbose_name="Account Status",
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class UserDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="detail")
    secondary_email = models.EmailField(null=True, blank=True, max_length=255)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(
        max_length=10, choices=GenderChoices.CHOICES, null=True, blank=True
    )
    marrital_status = models.CharField(
        max_length=255, choices=MarritialStatus.CHOICES, null=True, blank=True
    )
    bio = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "User Detail"
        verbose_name_plural = "User Details"

    @property
    def age(self):
        """
        Calculate the age of the user based on date_of_birth.
        """
        if self.date_of_birth:
            today = now().date().today()
            return (
                today.year
                - self.date_of_birth.year
                - (
                    (today.month, today.day)
                    < (self.date_of_birth.month, self.date_of_birth.day)
                )
            )
        return None

    @property
    def age_nicely(self):
        """
        Calculate the age of the user based on date_of_birth in a human-readable format.
        """
        if self.date_of_birth:
            today = now().date().today()
            return timesince.timesince(self.date_of_birth, today)
        return None


class Profile(models.Model):
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="profiles"
    )
    image = models.ImageField(upload_to=_user_profile_image)
    primary = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"


class Address(models.Model):
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="addresses"
    )
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True)
    pincode = models.IntegerField(null=True, blank=True)
    address_type = models.CharField(
        max_length=255, choices=AddressType.CHOICES, default=AddressType.HOME
    )


class EmergencyDetails(models.Model):
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="emergency_details"
    )
    name = models.CharField(max_length=255)
    phone_number = PhoneNumberField(null=True, blank=True, region="IN")
    relationship = models.CharField(max_length=255, choices=RelationshipChoices.CHOICES)

    class Meta:
        verbose_name = "Emergency Details"
        verbose_name_plural = "Emergency Details"


class SecurityQuestion(models.Model):
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="security_questions"
    )
    question = models.TextField(choices=QuestionChoices.CHOICES)
    answer = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Security Question"
        verbose_name_plural = "Security Questions"
        unique_together = ("user", "question")
