from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    class Meta:
        ordering = ['-created_on']

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self): return self.title
# Create your models here.
