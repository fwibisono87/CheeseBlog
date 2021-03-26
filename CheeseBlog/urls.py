"""CheeseBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home import views as homeviews
from custom_auth import views as authviews
from django.conf.urls import include, url
from blog.views import BlogDetail, newBlog, isDone, editForm, deleteBlog, addCommentToBlog

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeviews.home),
    path('my/', authviews.dashboard),
    path('register/', authviews.register),
    url(r"accounts/", include("django.contrib.auth.urls")),
    url("newblog/",  newBlog),
    url("newblog/isDone", isDone),
    path('<slug:slug>/', BlogDetail.as_view(), name="post_detail"),
    path("edit/<int:blog_id>", editForm, name="edit"),
    path('delete/<int:blog_id>', deleteBlog, name="delete"),
    path('post/<int:pk>/comment/', addCommentToBlog, name='newComment'),
]
