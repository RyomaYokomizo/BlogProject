from django.shortcuts import render, redirect
from .models import Blog
from .forms import BlogForm
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST

# Create your views here.
def home(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, 'Blogs/home.html', context)

def detail(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    context = {
        'blog': blog
    }
    return render(request, 'Blogs/detail.html', context)

def blog_form(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BlogForm
        context = {
            'form': form
            }
    return render(request, 'Blogs/new_blog.html', context)

@require_POST
def delete_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    blog.delete()
    return redirect('home')

def edit_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.method == "POST":
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BlogForm(instance=blog)
        context = {
            'form':form,
            'blog':blog
            }    
        return render(request, 'Blogs/edit_blog.html',context)
