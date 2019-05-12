from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'about/index.html')

def aboutPost(request):
    return render(request,'about/aboutPost.html')