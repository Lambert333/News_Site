from django.shortcuts import render
from .models import News
from django.http import *

def index(request):
    return render(request, 'main/index.html')

def news(request):
    news = News.objects.order_by('-date')
    return render(request, 'main/news.html', {'news': news})

def about(request):
    return render(request, 'main/about.html')

# Create your views here.
