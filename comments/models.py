from django.db import models
from django.db.models import CASCADE
from user.models import User
# Create your models here.
from posts.models import Post

class Comment(models.Model):
    content = models.TextField()
    created_at = models.TextField()
    user = models.ForeignKey(User, on_delete=CASCADE, null=True)
    post = models.ForeignKey(Post, on_delete=CASCADE, null=True)

