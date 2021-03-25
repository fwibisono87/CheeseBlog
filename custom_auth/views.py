from django.shortcuts import render
from django.contrib.auth import login
from django.urls import reverse
from django.shortcuts import redirect, render
from custom_auth.forms import CustomUserCreationForm
from blog.views import Blog


# Create your views here.
def dashboard(request):
    blog_posts = list(Blog.objects.filter(author=request.user))
    response = {'posts': set(blog_posts)}
    return render(request, "registration/mydashboard.html", response)


def register(request):
    if request.method == "GET":
        print("masuk get")
        return render(
            request, "registration/registration.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        print("masuk post")
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            print("form valid")
            user = form.save()
            login(request, user)
            return redirect("/my/")
    print("form fail")
    return render(
        request, "registration/registration.html",
        {"form": CustomUserCreationForm}
    )
