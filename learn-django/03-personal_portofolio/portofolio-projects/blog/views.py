from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
def post(request): 
    post = Blog.objects
    return render(request, 'blog.html',{'post':post})

def detail(request, blog_title): 
    # blog_title = blog_title.replace(' ', '-')
    blogdetail = get_object_or_404(Blog, pk=blog_title)
    return render(request, 'detail.html', {'blog': blogdetail})
