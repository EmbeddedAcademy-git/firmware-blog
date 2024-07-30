from django.db import models
from django.contrib.auth.models import User

class Image(models.Model):
    file = models.ImageField(upload_to='images/')

class Userprofile(models.Model):
    name = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='userprofile')
    bio = models.TextField()

class Tag(models.Model):
    tag = models.TextField(unique=True)
