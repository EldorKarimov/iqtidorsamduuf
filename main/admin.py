from django.contrib import admin

from .models import Carousel, StartUpProjects, TalentedStudents, Documents, Competition

admin.site.register(Carousel)
@admin.register(StartUpProjects)
class StartUpProjectsAdmin(admin.ModelAdmin):
    list_display = ['title', 'created', 'updated', 'is_available']
    list_editable = ('is_available', )
    search_fields = ('title', )
    list_filter = ('is_available', )
    ordering = ('-created', )
    prepopulated_fields = {"slug":('title', )}

@admin.register(TalentedStudents)
class TalentedStudentsAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'patronymic', 'teacher_full_name', 'talent_type', 'is_available')
    search_fields = ['first_name', 'last_name', 'patronymic', 'teacher_full_name']
    list_filter = ['is_available', 'talent_type']
    list_per_page = 20
    list_editable = ('is_available', 'talent_type')

@admin.register(Documents)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['file_name', 'created', 'updated']
    list_filter = ('doc_type', )
    search_fields = ['file_name']

@admin.register(Competition)
class CompetitionAdmin(admin.ModelAdmin):
    list_display = ['title', 'created', 'updated']
    search_fields = ['title']
    list_per_page = 20
    prepopulated_fields = {'slug':('title', )}
    