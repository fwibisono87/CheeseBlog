from django.shortcuts import render
from blog.models import Blog


def home(request):
    blog_posts = list(Blog.objects.all())
    response = {'posts': set(blog_posts)}
    return render(request, 'home.html', response)
# Create your views here.
