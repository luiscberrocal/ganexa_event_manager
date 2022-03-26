from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.
from model_utils.models import TimeStampedModel

from ganexa_event_manager.golf.managers import GolfClubManager


class GolfCourse(TimeStampedModel):
    name = models.CharField(_('Name'), max_length=80)
    short_name = models.CharField(_('Short name'), max_length=30)
    country = models.CharField(_('Country'), max_length=3, help_text=_('ISO 3166 country code'))

    def __str__(self):
        return self.short_name


class GolfClub(TimeStampedModel):
    player = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('Player'),
                               on_delete=models.CASCADE, related_name='golf_clubs')
    name = models.CharField(_('Name'), max_length=30)
    order = models.PositiveSmallIntegerField(_('Order'))

    objects = GolfClubManager()

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('player', 'name')
        ordering = ('order',)


class HitClassification(TimeStampedModel):
    order = models.PositiveSmallIntegerField(_('Order'))
    player = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('Player'),
                               on_delete=models.CASCADE, related_name='hit_classifications')
    name = models.CharField(_('Name'), max_length=30)
    hit_type = models.PositiveSmallIntegerField(_('Hit type'), default=1,
                                                help_text=_('Give 1 for a bad hit, 2 for a good hit'))

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('player', 'name')
        ordering = ('order',)


class RangeHit(TimeStampedModel):
    LEFT_DIRECTION = 'L'
    RIGHT_DIRECTION = 'R'
    STRAIGHT_DIRECTION = 'S'
    DIRECTION_CHOICES = (
        (LEFT_DIRECTION, _('Left')),
        (STRAIGHT_DIRECTION, _('Straight')),
        (RIGHT_DIRECTION, _('Right')),
    )
    course = models.ForeignKey(GolfCourse, verbose_name=_('Course'), on_delete=models.PROTECT,
                               related_name='range_hits')
    player = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('Player'),
                               on_delete=models.CASCADE, related_name='range_hits')
    club = models.ForeignKey(GolfClub, verbose_name=_('Club'), on_delete=models.PROTECT,
                             related_name='range_hits')
    distance = models.PositiveSmallIntegerField(_('Distance'))
    direction = models.CharField(_('Direction'), max_length=1, choices=DIRECTION_CHOICES)
    hit_classification = models.ForeignKey(HitClassification, verbose_name=_('Hit class'), on_delete=models.PROTECT,
                                           related_name='range_hits', null=True, blank=True)

    def __str__(self):
        return _(f'{self.created} distance: {self.distance} direction: {self.direction}')

    class Meta:
        ordering = ('created',)
