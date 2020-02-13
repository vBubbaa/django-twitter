from django import template
from tweets.models import Likes
from django.shortcuts import redirect

register = template.Library()

# Custom templatetag that returns T/F
# @params: tweet obj, user obj
# If the user has already liked the post than it returns false, else true
# Used to customize heart icons to filled or not filled depending on like status
@register.filter(name='check_if_liked')
def check_if_liked(tweet, user):
    return Likes.objects.filter(tweet=tweet, user=user).exists()
