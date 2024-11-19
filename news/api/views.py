from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from news.models import News, Tag, NewsCategory
from .serializers import NewsSerializer, CategorySerializer, TagSerializer
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from shared.pagination import CustomPageNumberPagination
from shared.utils import get_lang_code


class NewsListAPIView(APIView):
    @swagger_auto_schema(
        responses={
            200: openapi.Response(
                description="Successful Response",
                schema=NewsSerializer(many=True)
            )
        }
    )
    def get(self, request):
        news = News.objects.filter(is_published = True)
        paginator = CustomPageNumberPagination()
        page_obj = paginator.paginate_queryset(news, request)
        serializer = NewsSerializer(page_obj, many = True, context = get_lang_code(request))
        response = paginator.get_paginated_response(serializer.data)
        return Response(response, status=status.HTTP_200_OK)
    
class NewsCategoryListView(APIView):
    @swagger_auto_schema(
        responses={
            200: openapi.Response(
                description="Successful Response",
                schema=CategorySerializer(many=True)
            )
        }
    )
    def get(self, request):
        categories = NewsCategory.objects.all()
        serializer = CategorySerializer(categories, many = True)
        data = {
            'success':True,
            'data':serializer.data
        }
        return Response(data=data, status=status.HTTP_200_OK)
    
class NewsDetailAPIView(APIView):
    @swagger_auto_schema(
        responses={
            200: openapi.Response(
                description="news detail view",
                schema=NewsSerializer
            )
        }
    )
    def get(self, request, news_slug):
        new = get_object_or_404(News, slug = news_slug)
        serializer = NewsSerializer(new, context = get_lang_code(request))
        data = {
            'success': True,
            'data': serializer.data
        }
        return Response(
            data=data,
            status=status.HTTP_200_OK
        )
    
class NewsByCategoryAPIView(APIView):
    def get(self, request, cat_slug):
        category = get_object_or_404(NewsCategory, slug = cat_slug)
        news = News.objects.filter(category = category).order_by('-created')
        paginator = CustomPageNumberPagination()
        page_obj = paginator.paginate_queryset(news, request)
        serializer = NewsSerializer(page_obj, many = True, context = get_lang_code(request))
        return Response(
            paginator.get_paginated_response(serializer.data),
            status=status.HTTP_200_OK
        )

class NewsByTagAPIView(APIView):
    def get(self, request, tag_slug):
        tag = get_object_or_404(Tag, slug = tag_slug)
        news = News.objects.filter(tags = tag).order_by('-created')
        paginator = CustomPageNumberPagination()
        page_obj = paginator.paginate_queryset(news, request)
        serializer = NewsSerializer(page_obj, many = True, context = get_lang_code(request))
        return Response(
            paginator.get_paginated_response(serializer.data),
            status=status.HTTP_200_OK
        )