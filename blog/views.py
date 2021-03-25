from django.views import generic
from .models import Blog


class BlogDetail(generic.DetailView):
    model = Blog
    template_name = 'blogdetail.html'
