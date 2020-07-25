from django import template
from django.template.defaulttags import register

register = template.Library()

@register.filter(name='get_long')
def get_long(dictionary, key):
    return dictionary[key]["long"]

@register.filter(name='get_lat')
def get_lat(dictionary, key):
    return dictionary[key]["lat"]
