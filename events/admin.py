from django.contrib import admin

from .models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = ('game_name', 'get_time_date')
    search_fields = ('game_name', 'start_date')

    def get_time_date(self, obj):
        return f"{obj.start_date} {obj.start_time}"

    get_time_date.short_description = 'Date'

    list_filter = ["game_name"]


# Register your models here.
admin.site.register(Event, EventAdmin)
