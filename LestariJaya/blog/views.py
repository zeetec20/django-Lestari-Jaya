from django.shortcuts import render

def index(request):
    return render(request, 'blog/index.html')

def blogPost(request):
    return render(request, 'blog/blogPost.html')
