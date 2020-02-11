from django.db import models
from users.models import CustomUser
from django.utils import timezone
from django.conf import settings
from django.urls import reverse

# Tweet model that contains the text of the tweet and is connected to a user with a FK
class Tweet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='tweets', on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    text = models.CharField(max_length=200, blank=False, null=False)

    # Order by most recent always
    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.text

    # Builds absolute URL for a given tweet
    # @params: tweetid, username (both for URL building /user/tweetid)
    def get_absolute_url(self):
        return reverse('tweet', kwargs={
            'tweet_id': self.id,
            'username': self.user.username
        })

    # Method to get the total amount of likes
    def get_likes(self):
        return self.liked_tweet.count()

# Comment model that is tied to a user that wrote the comment, and the tweet it is commenting on
class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comments', on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, related_name='comments', on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    text = models.CharField(max_length=200, blank=False, null=False)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.text

# Like model tieing a user to a tweet that was liked
class Likes(models.Model):
    tweet = models.ForeignKey(Tweet, related_name='liked_tweet', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_liker', on_delete=models.CASCADE)
