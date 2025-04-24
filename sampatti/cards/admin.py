from utils.utils import get_model
from django.contrib import admin
from utils.constants import AppModel

Card = get_model(**AppModel.CARD)
GiftCard = get_model(**AppModel.GIFTCARD)


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    """Card Admin"""

    list_display = (
        "id",
        "card_number",
        "card_type",
        "expiry_date",
        "status",
        "created",
        "modified",
    )
    search_fields = ("card_number",)
    list_filter = ("card_type", "status")
    ordering = ("-created",)
    list_per_page = 20
    date_hierarchy = "created"
    list_editable = ("status",)
    actions = ["activate_cards", "deactivate_cards"]
    actions_on_top = True

    def activate_cards(self, request, queryset):
        """Activate selected cards"""
        queryset.update(is_active=True)
        self.message_user(request, "Selected cards have been activated.")

    activate_cards.short_description = "Activate selected cards"

    def deactivate_cards(self, request, queryset):
        """Deactivate selected cards"""
        queryset.update(is_active=False)
        self.message_user(request, "Selected cards have been deactivated.")

    deactivate_cards.short_description = "Deactivate selected cards"
