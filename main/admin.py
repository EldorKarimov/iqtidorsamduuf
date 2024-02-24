from django.contrib import admin

from .models import Carousel, StartUpProjects

admin.site.register(Carousel)
@admin.register(StartUpProjects)
class StartUpProjectsAdmin(admin.ModelAdmin):
    list_display = ['title', 'created', 'updated', 'is_available']
    list_editable = ('is_available', )
    search_fields = ('title', )
    list_filter = ('is_available', )
    ordering = ('-created', )
    prepopulated_fields = {"slug":('title', )}