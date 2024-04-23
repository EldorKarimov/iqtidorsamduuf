from django.urls import path
from . import views

urlpatterns = [
    path('carousels/', views.CarouselListAPIView.as_view()),
    path('start-up/', views.StartUpProjectsListApiView.as_view()),
    path('talent-students/list/', views.TalentedStudentsListAPIView.as_view()),
    path('talent-students/list/<str:talent_type>/', views.TalentedStudentsListAPIView.as_view()),
    path('docs/', views.DocumentsListAPIView.as_view()),
    path('docs/<str:doc_type>/', views.DocumentsListAPIView.as_view()),
    path('competitions/', views.CompetitionListAPIView.as_view())
]