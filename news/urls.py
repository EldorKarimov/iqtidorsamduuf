from django.urls import path
from . import views

app_name = 'news'
urlpatterns = [
    path('', views.NewsListView.as_view(), name = "news_list"),
    path('<slug:category_slug>/', views.NewsListView.as_view(), name = "news_by_category"),
    path('tag/<slug:tag_slug>/', views.NewsListView.as_view(), name = "news_by_tag"),
    path('<slug:category_slug>/<slug:news_slug>/', views.NewsDetailView.as_view(), name='news_detail')
]