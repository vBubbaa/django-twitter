from django.db import models
from users.models import CustomUser
from django.utils import timezone
from django.conf import settings

class Tweet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='tweets', on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    text = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.text
