from minerals.models import Mineral

from django import template

import random

register = template.Library()


@register.filter
def getattribute(obj, value):
    return getattr(obj, value)


@register.filter
def fieldname(obj, field_name):
    return obj._meta.get_field(field_name).verbose_name


@register.simple_tag
def random_pk():
    pk = random.randint (1, 874)
    return pk


@register.inclusion_tag('minerals/group_list.html')
def group_list(selected_group):
    groups = Mineral.objects.values_list('group', flat=True).distinct()
    return {'groups' : groups, 'selected_group': selected_group}