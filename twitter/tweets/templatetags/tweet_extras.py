from django import template
from tweets.models import Likes
register = template.Library()

@register.filter(name='check_if_liked')
def check_if_liked(tweet, user):
    return Likes.objects.filter(tweet=tweet, user=user).exists()
