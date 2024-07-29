from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from main.models import *
from django.utils.translation import gettext_lazy as _


class CarouselSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carousel
        fields = ('id', 'image', 'content', 'content2', 'created', 'updated')

class StartUpProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = StartUpProjects
        fields = ('title', 'slug', 'image', 'content', 'is_available', 'created', 'updated')
        extra_kwargs = {
            'id':{'read_only':True},
            'slug':{'read_only':True},
            'is_available':{'read_only':True},
        }

class TalentedStudentsSerializer(serializers.ModelSerializer):
    talent_type_display = serializers.ChoiceField(
        source='get_talent_type_display',
        choices=TalentedStudents.TYPE,
        read_only=True,
    )
    class Meta:
        model = TalentedStudents
        fields = ('id', 'first_name', 'last_name', 'patronymic', 'image', 'teacher_full_name', 'description', 'is_available', 'talent_type', 'talent_type_display', 'created', 'updated')

class DocumentsSerializer(serializers.ModelSerializer):
    doc_type_display = serializers.ChoiceField(
        source='get_doc_type_display',
        choices=Documents.DOC_TYPE,
        read_only=True,
    )
    class Meta:
        model = Documents
        fields = ('id', 'doc_type', 'doc_type_display', 'file_name', 'file', 'doc_date', 'created', 'updated')
    
class CompetitionSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    class Meta:
        model = Competition
        fields = ('id', 'title', 'slug', 'image', 'description')
        extra_kwargs = {
            'id':{'read_only':True}
        }

    def get_title(self, obj):
        lang_code = self.context.get('lang_code', 'uz')
        return getattr(obj, f"title_{lang_code}", obj.title)
    
    def get_title(self, obj):
        lang_code = self.context.get('lang_code', 'uz')
        return getattr(obj, f"description_{lang_code}", obj.description)