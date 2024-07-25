from rest_framework import serializers
from news.models import News, NewsCategory, Tag

class CategorySerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    class Meta:
        model = NewsCategory
        fields = ('id', 'name', 'slug', 'created', 'updated')
    
    def get_name(self, obj):
        lang_code = self.context.get('lang_code', 'uz')
        return getattr(obj, f"name_{lang_code}", obj.name)
    
class TagSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    class Meta:
        model = Tag
        fields = ('id', 'name', 'slug', 'created', 'updated')

    def get_name(self, obj):
        lang_code = self.context.get('lang_code', 'uz')
        return getattr(obj, f"name_{lang_code}", obj.name)


class NewsSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    tags = TagSerializer(many = True)
    user = serializers.SerializerMethodField()
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    
    class Meta:
        model = News
        fields = ['id', 'title', 'slug', 'image', 'description', 'category', 'tags', 'user', 'is_published']
        extra_kwargs = {
            'id':{'read_only': True},
            'category':{'read_only': True},
            'user':{'read_only': True},
            'tags':{'read_only': True},
        }
    
    def get_title(self, obj):
        lang_code = self.context.get('lang_code')
        return getattr(obj, f"title_{lang_code}", obj.title)

    def get_description(self, obj):
        lang_code = self.context.get('lang_code', 'uz')
        return getattr(obj, f"description_{lang_code}", obj.description)

    def get_user(self, obj):
        return {
            'id': obj.user.id,
            "full_name": obj.user.get_full_name()
        }
