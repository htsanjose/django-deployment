from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    # Create this to add attribute to User
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Additional attributes, blank=True: optional
    user_site = models.URLField(blank=True)
    user_pic = models.ImageField(upload_to='profile_pics', blank=True) # /media/profile_pics

    def __str__(self):
        return self.user.username
