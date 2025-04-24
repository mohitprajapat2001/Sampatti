from django.utils.translation import gettext_lazy as _


class GenderChoices:
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"

    CHOICES = (
        (MALE, _("Male")),
        (FEMALE, _("Female")),
        (OTHER, _("Other")),
    )


class RelationshipChoices:
    PARENT = "parent"
    SPOUSE = "spouse"
    SIBLING = "sibling"
    CHILD = "child"
    FRIEND = "friend"
    COLLEAGUE = "colleague"
    NEIGHBOR = "neighbor"
    OTHER = "other"
    EMERGENCY_CONTACT = "emergency_contact"
    CHOICES = (
        (PARENT, _("Parent")),
        (SPOUSE, _("Spouse")),
        (SIBLING, _("Sibling")),
        (CHILD, _("Child")),
        (FRIEND, _("Friend")),
        (COLLEAGUE, _("Colleague")),
        (NEIGHBOR, _("Neighbor")),
        (OTHER, _("Other")),
        (
            EMERGENCY_CONTACT,
            _("Emergency Contact"),
        ),
    )


class QuestionChoices:
    MOTHER_MAIDEN_NAME = "mother_maiden_name"
    PET_NAME = "pet_name"
    FIRST_SCHOOL = "first_school"
    FIRST_CAR = "first_car"
    FAVORITE_BOOK = "favorite_book"
    BEST_FRIEND = "best_friend"
    CITY_BORN = "city_born"
    FATHER_NAME = "father_name"
    GRANDPARENT_NAME = "grandparent_name"
    FAVORITE_SPORT = "favorite_sport"
    PREFER_NOT_TO_SAY = "prefer_not_to_say"

    CHOICES = (
        (MOTHER_MAIDEN_NAME, _("What is your mother's maiden name?")),
        (PET_NAME, _("What is the name of your first pet?")),
        (FIRST_SCHOOL, _("What is the name of your first school?")),
        (FIRST_CAR, _("What was the make of your first car?")),
        (FAVORITE_BOOK, _("What is your favorite book?")),
        (BEST_FRIEND, _("What is the name of your best friend?")),
        (CITY_BORN, _("In what city were you born?")),
        (FATHER_NAME, _("What is your father's name?")),
        (GRANDPARENT_NAME, _("What is the name of your maternal grandfather?")),
        (FAVORITE_SPORT, _("What is your favorite sport?")),
        (PREFER_NOT_TO_SAY, _("Prefer Not to Say")),
    )


class AccountStatus:
    ACTIVE = "active"
    INACTIVE = "inactive"
    SUSPENDED = "suspended"
    BANNED = "banned"

    CHOICES = (
        (ACTIVE, _("Active")),
        (INACTIVE, _("Inactive")),
        (SUSPENDED, _("Suspended")),
        (BANNED, _("Banned")),
    )


class MarritialStatus:
    SINGLE = "single"
    IN_A_RELATIONSHIP = "in_a_relationship"
    ENGAGED = "engaged"
    MARRIED = "married"
    SEPARATED = "separated"
    DIVORCED = "divorced"
    WIDOWED = "widowed"
    COMPLICATED = "complicated"
    PREFER_NOT_TO_SAY = "prefer_not_to_say"
    OTHER = "other"

    CHOICES = (
        (SINGLE, _("Single")),
        (IN_A_RELATIONSHIP, _("In a Relationship")),
        (ENGAGED, _("Engaged")),
        (MARRIED, _("Married")),
        (SEPARATED, _("Separated")),
        (DIVORCED, _("Divorced")),
        (WIDOWED, _("Widowed")),
        (COMPLICATED, _("It's Complicated")),
        (PREFER_NOT_TO_SAY, _("Prefer Not to Say")),
        (OTHER, _("Other")),
    )


class AddressType:
    HOME = "home"
    WORK = "work"
    OTHER = "other"

    CHOICES = (
        (HOME, _("Home")),
        (WORK, _("Work")),
        (OTHER, _("Other")),
    )
