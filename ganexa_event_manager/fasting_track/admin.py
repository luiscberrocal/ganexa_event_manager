from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import FastingSession


@admin.register(FastingSession)
class FastingSessionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'start_date',
        'end_date',
        'duration',
        'target_duration',
        'comments',
        'created',
        'modified',
        'created_by',
        'modified_by',
    )
    list_filter = (
        'user',
        'start_date',
        'end_date',
    )
    list_per_page = 20
