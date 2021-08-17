from django.db import models
from django.db.models import SET_NULL
from user.models import User
from categories.models import Category

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    slug = models.SlugField(max_length=255, unique=True)
    miniature = models.ImageField(upload_to='posts/images/')
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=SET_NULL, null=True) # cuando el usuario sea borrado el post no se va a borrar
    category = models.ForeignKey(Category, on_delete=SET_NULL, null=True)

    def __str__(self):
        return self.title
