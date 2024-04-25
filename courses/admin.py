from django.contrib import admin
from .models import Author, Course
from django import forms
from accounts.models import CustomUser

class AuthorAdminForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].queryset = CustomUser.objects.filter(is_staff=True)

class AuthorAdmin(admin.ModelAdmin):
    form = AuthorAdminForm
    list_display = ['user', 'bio']
    search_fields = ['user__username', 'user__first_name', 'user__last_name']
    list_filter = ['user__is_active']

admin.site.register(Author, AuthorAdmin)

class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'course_type', 'author']
    search_fields = ['title', 'slug', 'author__user__username']
    list_filter = ['course_type', 'author']

    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'content', 'youtube_link', 'course_type', 'author', 'file'),
        }),
    )

admin.site.register(Course, CourseAdmin)