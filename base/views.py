from django.shortcuts import render
from django.http import HttpResponse

# Views

def home(request):
    return render(request, 'base/index.html')

def posts(request):
    return render(request, 'base/posts.html')

def post(request):
    return render(request, 'base/post.html')

def profile(request):
    return render(request, 'base/profile.html')

def about(request):
    return render(request, 'base/about.html')
