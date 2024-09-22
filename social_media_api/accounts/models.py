from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(upload_to="profile_pics/", blank=True, null=True)
    following = models.ManyToManyField("self", related_name="following_set", symmetrical=False)
    followers = models.ManyToManyField("self", related_name="followers_set", symmetrical=False)

    def __str__(self):
        return self.username
