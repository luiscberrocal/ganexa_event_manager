# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Event, TimeSlot, Ticket


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'start_date',
        'end_date',
        'max_tickets_per_day',
        'created',
        'modified',
    )
    list_filter = ('created', 'modified', 'start_date', 'end_date')
    search_fields = ('name',)


@admin.register(TimeSlot)
class TimeSlotAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'event',
        'start_time',
        'end_time',
        'max_tickets',
        'created',
        'modified',
    )
    list_filter = ('created', 'modified', 'event', 'start_time', 'end_time')


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'event',
        'owner',
        'time_slot',
        'created',
        'modified',
    )
    list_filter = ('created', 'modified', 'event', 'owner', 'time_slot')
