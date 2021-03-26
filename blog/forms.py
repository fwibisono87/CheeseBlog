from .models import Blog, Comment
from django.forms import ModelForm


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = (
            'title',
            'content',
            'slug'
        )


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = (
            'author',
            'text'
        )
