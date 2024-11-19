from django.urls import path
from . import views

urlpatterns = [
    path('', views.NewsListAPIView.as_view()),
    path('categories/list/', views.NewsCategoryListView.as_view()),
    path('detail/<slug:news_slug>/', views.NewsDetailAPIView.as_view()),
    path('by/<slug:cat_slug>/', views.NewsByCategoryAPIView.as_view()),
    path('by/tag/<slug:tag_slug>/', views.NewsByTagAPIView.as_view())
]