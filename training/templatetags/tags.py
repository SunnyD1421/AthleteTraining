from django import template
from training.utils import *

register = template.Library()

@register.simple_tag
def getChartDataThrow(user):
    return getChartDataThrow(user)

@register.simple_tag
def getChartDataLift(user):
    return getChartDataLift(user)