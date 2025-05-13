from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model, models
from django.conf import settings
from utils.permissions import (
    EmployeePermissions,
    CustomerPermissions,
    AdminPermissions,
    ManagerPermissions,
)
from utils.constants import ManagementConstants
from utils.choices import GroupChoices

User = get_user_model()


class Command(BaseCommand):
    help = "Creates a superuser and sets initial settings"

    def handle(self, *args, **options):
        if not User.objects.filter(email=settings.ADMIN_EMAIL).exists():
            User.objects.create_superuser(
                username=settings.ADMIN_USER,
                password=settings.ADMIN_PASSWORD,
                email=settings.ADMIN_EMAIL,
            )
            self.stdout.write(
                self.style.SUCCESS(ManagementConstants.ADMIN_USER_CREATED_SUCCESSFULLY)
            )
        for group, _ in GroupChoices.CHOICES:
            instance = None
            if not models.Group.objects.filter(name=group).exists():
                instance = models.Group.objects.create(name=group)
                self.stdout.write(
                    self.style.SUCCESS(ManagementConstants.GROUP_CREATED % group)
                )
            if not instance:
                instance = models.Group.objects.get(name=group)
            if group == GroupChoices.SUPERUSER:
                instance.permissions.add(*AdminPermissions.get_permissions())
            elif group == GroupChoices.EMPLOYEE:
                instance.permissions.add(*EmployeePermissions.get_permissions())
            elif group == GroupChoices.CUSTOMER:
                instance.permissions.add(*CustomerPermissions.get_permissions())
            elif group == GroupChoices.MANAGER:
                instance.permissions.add(*ManagerPermissions.get_permissions())
            instance.save()
            self.stdout.write(
                self.style.SUCCESS(
                    ManagementConstants.GROUP_PERMISSIONS_ASSIGNED % group
                )
            )
        self.stdout.write(self.style.SUCCESS(ManagementConstants.INITIAL_SETTINGS_SET))
