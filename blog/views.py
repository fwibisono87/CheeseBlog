from django.views import generic
from .models import Blog
from .forms import BlogForm, CommentForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
import slugify
import random, string


def BlogDetail(request, slug):
    template_name = 'blogdetail.html'
    blog = get_object_or_404(Blog, slug=slug)
    comments = Blog.comments
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.blog = blog
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'blog': blog,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})


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


def isDone(request):
    return render(request, "isdone.html")

