from django import template
from ..models import News, Genre

register = template.Library()


@register.simple_tag()
def get_news():
    return News.objects.all().order_by('-views')[:7]

@register.simple_tag()
def get_genre():
    return Genre.objects.all()