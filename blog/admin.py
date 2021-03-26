from django.contrib import admin
from .models import Blog, Comment


class BlogAdmin(admin.ModelAdmin):
    ##fields displayed on admmin
    list_display = ('title', 'slug', 'created_on')
    ##searchable fields
    search_fields = ['title', 'content']
    ##auto-create slug field with title
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)
# Register your models here.
