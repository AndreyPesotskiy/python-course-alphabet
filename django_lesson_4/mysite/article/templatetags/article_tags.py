import random
from django import template

register = template.Library()

@register.simple_tag
def add_random_number(text):
    return text + '{}'.format(random.randint(1, 10))
