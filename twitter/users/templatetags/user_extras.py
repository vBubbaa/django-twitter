from django import template
from users.models import Follow
from django.shortcuts import redirect

register = template.Library()

# Custom templatetag that returns T/F
# @params: request user(followee), user (who to follow)
# Checks if the request user is following another user passed as @param
@register.filter(name='is_following')
def is_following(requser, user):
    return Follow.objects.filter(following=user, follower=requser).exists()
