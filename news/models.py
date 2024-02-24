from django.db import models
from shared.models import BaseModel
from accounts.models import CustomUser
from django.urls import reverse

class NewsCategory(BaseModel):
    name = models.CharField(max_length = 150)
    slug = models.SlugField(max_length = 150, unique = True)
    
    def __str__(self):
        return self.name
    
    def get_url(self):
        return reverse('news:news_by_category', args=[self.slug])
    
    class Meta:
        verbose_name = 'News Category'
        verbose_name_plural = 'News Categories'

class Tag(BaseModel):
    name = models.CharField(max_length = 150)
    slug = models.SlugField(max_length = 150, unique = True)

    def get_url(self):
        return reverse('news:news_by_tag', args=[self.slug])
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

class News(BaseModel):
    title = models.CharField(max_length = 150)
    slug = models.SlugField(max_length = 150, unique = True)
    image = models.ImageField(upload_to='news/image')
    description = models.TextField()
    category = models.ForeignKey(NewsCategory, on_delete = models.CASCADE)
    tags = models.ManyToManyField(Tag)
    user = models.ForeignKey(CustomUser, on_delete = models.SET_NULL, null = True)
    is_published = models.BooleanField(default = False)

    def get_url(self):
        return reverse('news:news_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'New'
        verbose_name_plural = 'News'