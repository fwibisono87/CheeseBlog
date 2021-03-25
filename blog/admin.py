from django.contrib import admin
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    ##fields displayed on admmin
    list_display = ('title', 'slug', 'status','created_on')
    ##available filters
    list_filter = ("status",)
    ##searchable fields
    search_fields = ['title', 'content']
    ##auto-create slug field with title
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Blog, BlogAdmin)
# Register your models here.
