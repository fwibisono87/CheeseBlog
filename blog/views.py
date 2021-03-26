import random
import string

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic

from .forms import BlogForm, CommentForm
from .models import Blog


class BlogDetail(generic.DetailView):
    model = Blog
    template_name = 'blogdetail.html'


@login_required
def newBlog(request):
    if request.method == 'POST':
        print("form posts!")
        form = BlogForm(request.POST or None)
        form.slug = "thisIsJustATemporarySlug"
        if form.is_valid():
            print("form is valid!")
            submission = form.save(commit=False)
            submission.author = request.user
            form.save()
            return render(request, 'isdone.html')
        print("form invalid!")
    else:
        ##the goal of this random string generator is to generate slugs
        ##a stupid fix to eliminate invalid slug erroes, but it works, so TOO BAD! :D
        letters = string.ascii_letters
        random_slug = ''.join(random.choice(letters) for i in range(20))
        form = BlogForm(initial={'slug': random_slug})
    context = {'form': form}
    return render(request, 'newblog.html', context)


def editForm(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    if request.method == "POST":
        form = BlogForm(request.POST or None)
        if form.is_valid():
            print("form is valid!")
            edit = form.save(commit=False)
            blog.title = edit.title
            blog.content = edit.content
            blog.save()
            return redirect('post_detail', blog.slug)
        else:
            print("form invalid")
            print(form.errors)
    else:
        form = BlogForm(initial={'title': blog.title, 'content': blog.content, 'slug': blog.slug})
    context = {'form': form, 'blog': blog}
    return render(request, 'newblog.html', context)


def deleteBlog(request, blog_id):
    target_blog = Blog.objects.get(pk=blog_id)
    if target_blog:
        if target_blog.author == request.user:
            target_blog.delete()
            context = {'status': 'done'}
        else:
            context = {'status': 'not_authorized'}
    else:
        context = {'status': 'not_exist'}
    return render(request, 'deleted.html', context=context)


def addCommentToBlog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == "POST":
        print("in post!")
        form = CommentForm(request.POST)
        if form.is_valid():
            print("form valid")
            comment = form.save(commit=False)
            comment.post = blog
            comment.save()
            return redirect('post_detail', blog.slug)
        else:
            print("form invalid")
    else:
        form = CommentForm
    return render(request, 'newComment.html', {'form': form})


def isDone(request):
    return render(request, "isdone.html")
