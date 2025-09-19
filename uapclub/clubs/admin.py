from django.contrib import admin
from .models import Club

@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ('name','short_name','created_at')
    search_fields = ('name','short_name')

