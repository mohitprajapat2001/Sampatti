from abc import ABC, abstractmethod
from django.contrib.auth.models import Permission


class UserPermissions(ABC):
    @abstractmethod
    def get_permissions():
        pass


class AdminPermissions(UserPermissions):
    def get_permissions():
        return Permission.objects.all().values_list("id", flat=True)


class ManagerPermissions(UserPermissions):
    def get_permissions():
        return (
            Permission.objects.filter(codename__contains="view").values_list(
                "id", flat=True
            )
            | Permission.objects.filter(codename__contains="add").values_list(
                "id", flat=True
            )
            | Permission.objects.filter(codename__contains="change").values_list(
                "id", flat=True
            )
        ).distinct()


class EmployeePermissions(UserPermissions):
    def get_permissions():
        return (
            Permission.objects.filter(codename__contains="view").values_list(
                "id", flat=True
            )
            | Permission.objects.filter(codename__contains="add").values_list(
                "id", flat=True
            )
        ).distinct()


class CustomerPermissions(UserPermissions):
    def get_permissions():
        return (
            Permission.objects.filter(codename__contains="view").values_list(
                "id", flat=True
            )
            | Permission.objects.filter(
                codename__in=[
                    "change_user",
                    "change_userdetail",
                    "add_profile",
                    "change_profile",
                    "add_address",
                    "change_address",
                    "delete_address",
                    "add_emergencydetails",
                    "change_emergencydetails",
                    "delete_emergencydetails",
                    "add_securityquestion",
                    "change_securityquestion",
                    "delete_securityquestion",
                ]
            ).values_list("id", flat=True)
        ).distinct()


abc = AdminPermissions()
