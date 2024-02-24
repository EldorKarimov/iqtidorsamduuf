from django.db import models
from shared.models import BaseModel

class Carousel(BaseModel):
    image = models.ImageField(upload_to='carousel',verbose_name='Rasm')
    content = models.CharField(max_length = 150, null = True, blank = True, verbose_name = "matn 1")
    content2 = models.CharField(max_length = 255, null = True, blank = True, verbose_name = "matn 2")

    def __str__(self):
        return self.content
    
    class Meta:
        verbose_name = 'Karusel'
        verbose_name_plural = 'Karusellar'

class StartUpProjects(BaseModel):
    title = models.CharField(max_length = 150, unique = True, verbose_name = "sarlavha")
    slug = models.SlugField(max_length = 150, unique = True)
    image = models.ImageField(upload_to='startup/images', verbose_name="Rasm")
    content = models.TextField(verbose_name = "Loyiha ta'rifi")
    is_available = models.BooleanField(default = False, verbose_name = "mavjudligi")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Start Up loyiha"
        verbose_name_plural = "Start Up loyihalar"