from django.shortcuts import render, get_object_or_404
from news.models import *
from .models import Carousel, StartUpProjects, TalentedStudents, Documents, Competition
from django.views import View

def home(request):
    news = News.objects.filter(is_published = True).order_by('-created')[:4]
    startupProjects = StartUpProjects.objects.filter(is_available = True)
    documents = Documents.objects.all().order_by('-created')[:6]
    carousels = Carousel.objects.all()
    competitions = Competition.objects.all().order_by('-created')[:4]
    context = {
        'news':news,
        'carousels':carousels,
        'startupProjects':startupProjects,
        'documents':documents,
        'competitions':competitions
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
    

class CompetitionListView(View):
    def get(self, request):
        competition = Competition.objects.all().order_by('-created')
        context = {
            'competitions':competition
        }
        return render(request, 'competition-list.html', context)

class CompetitionDetailView(View):
    def get(self, request, comp_slug):
        competition = Competition.objects.get(slug = comp_slug)
        context = {
            'competition':competition
        }
        return render(request, 'competition-detail.html', context)