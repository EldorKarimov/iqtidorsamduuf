from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.home, name='home'),
    path('iqtidorli-talabalar-royxati/', views.TalentStudentListView.as_view(), name="talent_students_list"),
    path('tanlovlar/', views.CompetitionListView.as_view(), name='competition_list'),
    path('tanlovlar/<slug:comp_slug>/', views.CompetitionDetailView.as_view(), name="competition_detail")
]