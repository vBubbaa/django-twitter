from django.db import models
from users.models import CustomUser
from django.utils import timezone
from django.conf import settings

class Tweet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='tweets', on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    text = models.CharField(max_length=200, blank=False, null=False)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return str(self.user.username) + '/' + str(self.pk)

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comments', on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, related_name='comments', on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    text = models.CharField(max_length=200, blank=False, null=False)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.text
        
