from django.shortcuts import render, redirect
from .models import Post

def home(request):
    Posts = Post.objects.all()
    return render(request, 'blog\home.html', {'posts': Posts})