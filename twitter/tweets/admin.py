from django.contrib import admin
from tweets.models import Tweet, Comment, Likes

admin.site.register(Tweet)
admin.site.register(Comment)
admin.site.register(Likes)
