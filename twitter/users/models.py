from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.conf import settings

# Custom user model inherting from the AbstractUser class built into Django
class CustomUser(AbstractUser):
    bio = models.TextField(max_length=264)
    location = models.CharField(max_length=128, blank=True, null=True)
    website = models.URLField(max_length=128, blank=True, null=True)
    profilepicture = models.FileField(upload_to='profile_picture', default='nopic.jpeg')

    def __str__(self):
        return self.username

    # Created the absolute url for a user
    # @params: username (it is unique)
    def get_absolute_url(self):
        return reverse('useroverview', kwargs={
            'username': self.username
        })

# Follow model that keeps track of user follows
class Follow(models.Model):
    following = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='following',on_delete=models.CASCADE)
    follower = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='follower',on_delete=models.CASCADE)
