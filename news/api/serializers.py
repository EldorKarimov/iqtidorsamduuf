from rest_framework import serializers
from news.models import News, NewsCategory, Tag

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsCategory
        fields = ('id', 'name', 'slug', 'created', 'updated')
    
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name', 'slug', 'created', 'updated')


class NewsSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    tags = TagSerializer(many = True)
    user = serializers.SerializerMethodField()
    
    class Meta:
        model = News
        fields = ['id', 'title', 'slug', 'image', 'description', 'category', 'tags', 'user', 'is_published']
        extra_kwargs = {
            'id':{'read_only': True},
            'category':{'read_only': True},
            'user':{'read_only': True},
            'tags':{'read_only': True},
        }

    def get_user(self, obj):
        return {
            'id': obj.user.id,
            "full_name": obj.user.get_full_name()
        }
