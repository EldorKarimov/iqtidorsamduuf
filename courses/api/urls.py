from django.urls import path
from . import views

urlpatterns = [
    path('<str:course_type>/', views.CourseListAPIView.as_view())
]