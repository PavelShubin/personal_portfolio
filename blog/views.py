from django.shortcuts import render
from .models import Blog

def all_blogs(request):
    blogs = Blog.objects.all()
    amount_of_blogs = len(blogs)
    return render(request, 'blog/all_blogs.html', {'amount_of_blogs': amount_of_blogs,
                                                   'blogs': blogs})