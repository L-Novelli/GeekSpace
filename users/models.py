from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    pfp = models.ImageField(default ="default.jpg", upload_to='media/profile_images')
    

    def __str__(self):
        return self.user.username