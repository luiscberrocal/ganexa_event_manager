# Register your models here.
# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import ExerciseProfile, Exercise, UserExercise, ExerciseSession
from ..core.mixins import AuditableAdminMixin


@admin.register(ExerciseProfile)
class ExerciseProfileAdmin(AuditableAdminMixin, admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'dob',
        'weight_units',
        'weight',
        'height_units',
        'height',
        'metadata',
        'created',
        'modified',
        'created_by',
        'modified_by',
    )
    list_filter = (
        'created',
        'modified',
        'created_by',
        'modified_by',
        'user',
        'dob',
    )


@admin.register(Exercise)
class ExerciseAdmin(AuditableAdminMixin, admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'force_type',
        'machine',
        'created',
        'modified',
        'created_by',
        'modified_by',
    )
    list_filter = (
        'created',
        'modified',
        'created_by',
        'modified_by',
        'machine',
    )
    search_fields = ('name',)


@admin.register(UserExercise)
class UserExerciseAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'display_order',
        'user',
        'exercise',
        'created',
        'modified',
    )
    list_filter = ('created', 'modified', 'user', 'exercise')


@admin.register(ExerciseSession)
class ExerciseSessionAdmin(AuditableAdminMixin, admin.ModelAdmin):
    list_display = (
        'id',
        'date',
        'user',
        'exercise',
        'units',
        'reps',
        'created',
        'modified',
        'created_by',
        'modified_by',
    )
    list_filter = (
        'created',
        'modified',
        'created_by',
        'modified_by',
        'date',
        'user',
        'exercise',
    )
