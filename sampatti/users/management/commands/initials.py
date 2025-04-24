from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model()


class Command(BaseCommand):
    help = "Creates a superuser and sets initial settings"

    def handle(self, *args, **options):
        if not User.objects.filter(username=settings.ADMIN_USER).exists():
            User.objects.create_superuser(
                username=settings.ADMIN_USER,
                password=settings.ADMIN_PASSWORD,
                email=settings.ADMIN_EMAIL,
            )
            self.stdout.write(
                self.style.SUCCESS(
                    f"Superuser {settings.ADMIN_USER} created successfully."
                )
            )
