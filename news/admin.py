from django.contrib import admin
from .models import News, NewsCategory, Tag

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'user', 'created', 'updated', 'is_published')
    list_editable = ('is_published', )
    list_filter = ('category', 'tags')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created', 'updated')
    filter_horizontal = ('tags',)


class NewsCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(News, NewsAdmin)
admin.site.register(NewsCategory, NewsCategoryAdmin)
admin.site.register(Tag, TagAdmin)
