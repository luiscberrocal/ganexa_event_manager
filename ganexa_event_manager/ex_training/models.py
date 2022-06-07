from enum import Enum

from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
# Create your models here.
from model_utils.models import TimeStampedModel

from ..core.models import AuditableModel


class WeightUnit(Enum):
    KG = _('Kilograms')
    LB = _('Pounds')


class HeightUnit(Enum):
    M = _('Meter')
    FT = _('Feet')


class ExerciseProfile(AuditableModel, TimeStampedModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name=_('User'), on_delete=models.CASCADE,
                                related_name='exercise_profile')
    dob = models.DateField(_('Date of birth'), null=True, blank=True)
    weight_units = models.CharField(_('Weight units'), max_length=2, default=WeightUnit.LB,
                                    choices=[(tag.name, tag.value) for tag in WeightUnit])
    weight = models.FloatField(_('Weight'))
    height_units = models.CharField(_('Height units'), max_length=2, default=HeightUnit.M,
                                    choices=[(tag.name, tag.value) for tag in HeightUnit])
    height = models.FloatField(_('Height'), default=1)
    metadata = models.JSONField(_('Metadata'), null=True, blank=True)

    def __str__(self):
        return f'Profile {self.user.username}'


class Exercise(AuditableModel, TimeStampedModel):
    name = models.CharField(_('Name'), max_length=80)
    force_type = models.SmallIntegerField(_('Force type'), default=1,
                                          help_text=_('1 for normal weight exercises, 0 for non weight exercises '
                                                      'and -1 for assisted exercises'))
    machine = models.BooleanField(_('Machine assisted'), default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class UserExercise(TimeStampedModel):
    display_order = models.PositiveSmallIntegerField(_('Display order'), default=1)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('User'), related_name='user_exercises',
                             on_delete=models.PROTECT)
    exercise = models.ForeignKey(Exercise, verbose_name=_('Exercise'), related_name='user_exercises',
                                 on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.display_order} {self.exercise.name} {self.user.username}'

    class Meta:
        ordering = ('display_order',)


class ExerciseSession(AuditableModel, TimeStampedModel):
    date = models.DateTimeField(_('date'), default=timezone.now())
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('User'), related_name='exercise_sessions',
                             on_delete=models.PROTECT)
    exercise = models.ForeignKey(Exercise, verbose_name=_('Exercise'), related_name='exercise_sessions',
                                 on_delete=models.PROTECT)
    units = models.CharField(_('Units'), max_length=2, default=WeightUnit.LB,
                             choices=[(tag.name, tag.value) for tag in WeightUnit])
    reps = models.PositiveSmallIntegerField(_('Reps'), default=1)

    def __str__(self):
        return f'{self.date} {self.user.username} {self.exercise.name}'

    class Meta:
        ordering = ('-date',)
