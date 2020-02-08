from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    bio = models.TextField(max_length=264)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return str(self.username) + '/'
