from django import template

register = template.Library()


@register.filter(name='contains_substring')
def contains_substring(iterable, substring):
    return any(substring in item for item in iterable)