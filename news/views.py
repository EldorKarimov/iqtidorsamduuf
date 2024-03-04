from django.shortcuts import render, get_object_or_404
from django.views import View
from hitcount.utils import get_hitcount_model
from hitcount.views import HitCountMixin

from .models import News, NewsCategory, Tag

class NewsListView(View):
    def get(self, request, category_slug = None, tag_slug = None):
        category = None
        tag = None
        if category_slug is not None:
            category = get_object_or_404(NewsCategory, slug = category_slug)
            news = News.objects.filter(is_published = True, category = category).order_by('-created')
        elif tag_slug is not None:
            tag = get_object_or_404(Tag, slug = tag_slug)
            news = News.objects.filter(is_published = True, tags = tag).order_by('-created')
        else:
            news = News.objects.filter(is_published = True).order_by('-created')
        context = {
            'news':news,
            'category':category,
            'tag':tag
        }
        
        return render(request, 'news/news-list.html', context)
        
class NewsDetailView(View):
    def get(self, request, category_slug, news_slug):
        categories = NewsCategory.objects.all()
        tags = Tag.objects.all()
        latest_news = News.objects.filter(is_published = True).order_by('-created')[:3]
        new = get_object_or_404(News, category__slug = category_slug, slug = news_slug)
        
        context = {
            'new':new,
            'categories': categories,
            'latest_news': latest_news,
            'tags':tags,
        }
        return render(request, 'news/detail.html', context)