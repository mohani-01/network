from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='poster')
    post = models.TextField()
    date = models.DateField(auto_now_add=True)
    like = models.IntegerField(default=0)
    views = models.IntegerField(default=0)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commenter')
    comment = models.TextField()
    time = models.DateField()
    posts = models.ManyToManyField(Post, blank=True, related_name="comment")
    
