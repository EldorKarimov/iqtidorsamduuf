from django.shortcuts import render, get_object_or_404
from news.models import *
from .models import Carousel, StartUpProjects
from django.views import View

def home(request):
    news = News.objects.filter(is_published = True).order_by('-created')
    carousels = Carousel.objects.all()
    context = {
        'news':news,
        'carousels':carousels
    }
    return render(request, 'home.html', context)