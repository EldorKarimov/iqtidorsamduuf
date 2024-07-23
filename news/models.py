from django.db import models
from shared.models import BaseModel
from accounts.models import CustomUser
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.translation import gettext_lazy as _

class NewsCategory(BaseModel):
    name = models.CharField(max_length = 150, verbose_name=_("name"))
    slug = models.SlugField(max_length = 150, unique = True)
    
    def __str__(self):
        return self.name
    
    def get_url(self):
        return reverse('news:news_by_category', args=[self.slug])
    
    class Meta:
        verbose_name = _('News Category')
        verbose_name_plural = _('News Categories')

class Tag(BaseModel):
    name = models.CharField(max_length = 150, verbose_name = _("name"))
    slug = models.SlugField(max_length = 150, unique = True)

    def get_url(self):
        return reverse('news:news_by_tag', args=[self.slug])
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')

class News(BaseModel):
    title = models.CharField(max_length = 150, verbose_name=_("title"))
    slug = models.SlugField(max_length = 150, unique = True)
    image = models.ImageField(upload_to='news/image', verbose_name=_("image"))
    description = RichTextUploadingField(verbose_name=_("description"))
    category = models.ForeignKey(NewsCategory, on_delete = models.CASCADE, verbose_name=_("category"))
    tags = models.ManyToManyField(Tag, verbose_name=_("tags"))
    user = models.ForeignKey(CustomUser, on_delete = models.SET_NULL, null = True, verbose_name=_("user"))
    is_published = models.BooleanField(default = False, verbose_name=_("is published"))

    def get_url(self):
        return reverse('news:news_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = _('New')
        verbose_name_plural = _('News')