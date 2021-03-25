from django.contrib import admin
from .models import Blog, Comment

class BlogAdmin(admin.ModelAdmin):
    ##fields displayed on admmin
    list_display = ('title', 'slug', 'created_on')
    ##searchable fields
    search_fields = ['title', 'content']
    ##auto-create slug field with title
    prepopulated_fields = {'slug': ('title',)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on')
    search_fields = ('name', 'body')

admin.site.register(Blog, BlogAdmin)
# Register your models here.
