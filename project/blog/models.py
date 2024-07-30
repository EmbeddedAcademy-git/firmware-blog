from django.db import models
from core.models import *

class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    thumbnail_image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='blogs')
    title = models.TextField()
    body = models.TextField()
    author = models.ForeignKey(Userprofile, on_delete=models.CASCADE, related_name='blogs')
    time_posted = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

class ReadingList(models.Model):
    user = models.ForeignKey(Userprofile, on_delete=models.CASCADE, related_name='reading_list')
    posts = models.ManyToManyField(Blog)
