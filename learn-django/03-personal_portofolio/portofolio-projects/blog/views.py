from django.shortcuts import render
from .models import Blog

# Create your views here.
def post(request): 
    post = Blog.objects
    return render(request, 'blog.html',{'post':post})