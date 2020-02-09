from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

class CustomUser(AbstractUser):
    bio = models.TextField(max_length=264)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('useroverview', kwargs={
            'username': self.username
        })
