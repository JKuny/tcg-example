from django.contrib import admin

from .models import Player


class PlayerAdmin(admin.ModelAdmin):
    list_display = ("get_full_name", "get_email", "phone_number", "preferred_game")
    search_fields = ("user__first_name", "user__last_name", "user__email")

    def get_full_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"

    def get_email(self, obj):
        return obj.user.email

    get_full_name.short_description = "Full Name"
    get_email.short_description = "Email"

    list_filter = ["preferred_game"]


# Register your models here.
admin.site.register(Player, PlayerAdmin)
