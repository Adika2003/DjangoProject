from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title','club','start_time','published')
    list_filter = ('club','published')
    search_fields = ('title','description')
