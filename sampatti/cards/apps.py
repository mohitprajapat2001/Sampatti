from django.apps import AppConfig


class CardsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "cards"

    def ready(self):
        super().ready()
        import cards.signals  # noqa F401
