from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.home, name='home'),
    path('iqtidorli-talabalar-royxati/', views.TalentStudentListView.as_view(), name="talent_students_list")
]