from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from news.models import News, Tag, NewsCategory
from .serializers import NewsSerializer, CategorySerializer, TagSerializer
from django.shortcuts import get_object_or_404

class NewsListAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        news = News.objects.filter(is_published = True)
        serializer = NewsSerializer(news, many = True)
        data = {
            'success': True,
            'data': serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)
    
class NewsDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, news_slug):
        new = get_object_or_404(News, slug = news_slug)
        serializer = NewsSerializer(new)
        data = {
            'success': True,
            'data': serializer.data
        }
        return Response(
            data=data,
            status=status.HTTP_200_OK
        )
    
class NewsByCategoryAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, cat_slug):
        category = get_object_or_404(NewsCategory, slug = cat_slug)
        news = News.objects.filter(category = category).order_by('-created')
        serializer = NewsSerializer(news, many = True)
        data = {
            'success': True,
            'news': serializer.data
        }
        return Response(
            data=data,
            status=status.HTTP_200_OK
        )

class NewsByTagAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, tag_slug):
        tag = get_object_or_404(Tag, slug = tag_slug)
        news = News.objects.filter(tags = tag).order_by('-created')
        serializer = NewsSerializer(news, many = True)
        data = {
            'success': True,
            'news': serializer.data
        }
        return Response(
            data=data,
            status=status.HTTP_200_OK
        )