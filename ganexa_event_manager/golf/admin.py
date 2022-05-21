# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import GolfCourse, GolfClub, HitClassification, RangeHit


@admin.register(GolfCourse)
class GolfCourseAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created',
        'modified',
        'name',
        'short_name',
        'country',
    )
    list_filter = ('created', 'modified')
    search_fields = ('name',)


@admin.register(GolfClub)
class GolfClubAdmin(admin.ModelAdmin):
    list_display = ('id', 'player', 'name', 'order', 'created', 'modified')
    list_filter = ('created', 'modified', 'player')
    search_fields = ('name',)


@admin.register(HitClassification)
class HitClassificationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'order',
        'player',
        'name',
        'hit_type',
        'created',
        'modified',
    )
    list_filter = ('created', 'modified', 'player')
    search_fields = ('name',)


@admin.register(RangeHit)
class RangeHitAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'course',
        'player',
        'club',
        'distance',
        'direction',
        'hit_classification',
        'created',
        'modified',
    )
    list_filter = (
        'course',
        'player',
    )
