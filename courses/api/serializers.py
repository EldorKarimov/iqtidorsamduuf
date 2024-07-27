from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from courses.models import Author, Course

class AuthorSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()
    phone = serializers.SerializerMethodField()
    bio = serializers.SerializerMethodField()
    class Meta:
        model = Author
        fields = ('id', 'full_name', 'email', 'phone', 'bio')

    def get_full_name(self, obj):
        return obj.user.get_full_name()
    
    def get_email(self, obj):
        return obj.user.email
    
    def get_phone(self, obj):
        return obj.user.phone
    
    def get_bio(self, obj):
        lang_code = self.context.get('lang_code', 'uz')
        return getattr(obj, f"bio_{lang_code}", obj.bio)
    
class CourseSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    title = serializers.SerializerMethodField()
    content = serializers.SerializerMethodField()
    course_type_display = serializers.ChoiceField(
        source = 'get_course_type_display',
        choices = Course.COURSE_TYPE,
        read_only = True
    )
    class Meta:
        model = Course
        fields = ('id', 'title', 'slug', 'content', 'youtube_link', 'course_type',
                  'course_type_display', 'author', 'file')
        
    def get_title(self, obj):
        lang_code = self.context.get("lang_code", "uz")
        return getattr(obj, f"title_{lang_code}", obj.title)
    
    def get_content(self, obj):
        lang_code = self.context.get("lang_code", "uz")
        return getattr(obj, f"content_{lang_code}", obj.content)