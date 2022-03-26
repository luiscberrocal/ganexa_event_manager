from django import template

register = template.Library()


@register.filter(name='is_golfer')
def is_golfer(user):
    return user.groups.filter(name='Golfers').exists()
