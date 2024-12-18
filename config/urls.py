from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve 
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


schema_view = get_schema_view(
   openapi.Info(
      title="SamduUF iqtidorli talabalar API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="karimoveldor19021@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=False,
#    permission_classes=(permissions.IsAuthenticatedOrReadOnly,),
)

api_urls = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/v1/auth/', include('accounts.api.urls')),
    path('api/v1/news/', include('news.api.urls')),
    path('api/v1/main/', include('main.api.urls')),
    path('api/v1/courses/', include('courses.api.urls')),
]

urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    # path('', include('main.urls')),
    # path('yangiliklar/', include('news.urls')),


    # api documentation 
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] + api_urls

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)