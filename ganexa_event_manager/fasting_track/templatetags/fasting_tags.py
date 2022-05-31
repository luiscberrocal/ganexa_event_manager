from django import template
from django.utils.translation import ugettext_lazy as _

register = template.Library()


def percentage(value):
    return '{0:.2%}'.format(value)


def hours(value):
    hours_text = _('hours')
    hours_template = '{0:,.2f}'
    hours_value = hours_template.format(value)
    return f'{hours_value} {hours_text}'



register.filter('percentage', percentage)
register.filter('hours', hours)
