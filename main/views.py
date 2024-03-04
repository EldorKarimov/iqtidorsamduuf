from django.shortcuts import render, get_object_or_404
from news.models import *
from .models import Carousel, StartUpProjects, TalentedStudents, Documents
from django.views import View

def home(request):
    news = News.objects.filter(is_published = True).order_by('-created')
    startupProjects = StartUpProjects.objects.filter(is_available = True)
    documents = Documents.objects.all().order_by('-created')[:6]
    carousels = Carousel.objects.all()
    context = {
        'news':news,
        'carousels':carousels,
        'startupProjects':startupProjects,
        'documents':documents
    }
    return render(request, 'home.html', context)

class TalentStudentListView(View):
    def get(self, request):
        talent_student_choice = request.GET.get('talent_student_choice')
        if talent_student_choice:
            talent_students = TalentedStudents.objects.filter(is_available = True, talent_type = talent_student_choice)
        else:
            talent_students = TalentedStudents.objects.filter(is_available = True)
        context = {
            'talent_students':talent_students
        }
        return render(request, 'talent_students_list.html', context)