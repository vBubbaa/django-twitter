from django.db import models
from users.models import CustomUser
from django.utils import timezone
from django.conf import settings
from django.urls import reverse

class Tweet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='tweets', on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    text = models.CharField(max_length=200, blank=False, null=False)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('tweet', kwargs={
            'tweet_id': self.id,
            'username': self.user.username
        })

    def get_likes(self):
        return self.liked_tweet.count()

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comments', on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, related_name='comments', on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    text = models.CharField(max_length=200, blank=False, null=False)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.text

class Likes(models.Model):
    tweet = models.ForeignKey(Tweet, related_name='liked_tweet', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_liker', on_delete=models.CASCADE)

    def check_if_liked(self, usercheck):
        if self.user.get(usercheck).exists():
            return True
        else:
            return False
