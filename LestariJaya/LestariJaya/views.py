from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'judulPage':['Home','Blog','About']
    }
    return render(request,'index.html', context)

