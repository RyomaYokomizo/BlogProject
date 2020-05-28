from django.contrib import admin
from .models import Blog

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'text', 'created_date')
    list_display_link = ('id', 'title')

admin.site.register(Blog, BlogAdmin)
