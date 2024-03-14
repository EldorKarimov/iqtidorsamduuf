from django.db import models
from shared.models import BaseModel
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse

class Carousel(BaseModel):
    image = models.ImageField(upload_to='carousel',verbose_name='Rasm')
    content = models.CharField(max_length = 150, null = True, blank = True, verbose_name = "matn 1")
    content2 = models.CharField(max_length = 255, null = True, blank = True, verbose_name = "matn 2")

    
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

class TalentedStudents(BaseModel):
    TYPE = (
        ('PRESIDENT', "Prezident"),
        ('STATE', "Davlat stipendiatlar"),
        ('TALENT', "Iqtidorli talabalar")
    )
    first_name = models.CharField(max_length = 150, verbose_name = "ism")
    last_name = models.CharField(max_length = 150, verbose_name = "Familiya")
    patronymic = models.CharField(max_length = 150, verbose_name = "Otasining ismi")
    image = models.ImageField(upload_to='talent-tudent/images', null=True, blank=True, verbose_name="Talaba rasmi")
    teacher_full_name = models.CharField(max_length = 255, verbose_name = "O'qituvchi F.I.SH")
    description = models.TextField(null = True, blank = True, verbose_name = "Talaba haqida ma'lumot")
    is_available = models.BooleanField(default = False)
    talent_type = models.CharField(max_length = 15, choices = TYPE, default = 'TALENT')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name = "Iqtidorli talaba"
        verbose_name_plural = "Iqtidorli talabalar"

class Documents(BaseModel):
    DOC_TYPE = (
        (1, "Buyruqlar"),
        (2, "Nizomlar"),
    )
    doc_type = models.PositiveSmallIntegerField(choices = DOC_TYPE, verbose_name = "Hujjat turi")
    file_name = models.CharField(max_length = 255, verbose_name = "hujjat nomi")
    file = models.FileField(upload_to='uploads/doc/files', verbose_name="fayl")
    doc_date = models.DateTimeField(default = timezone.now())

    def __str__(self):
        return self.file_name   
    
    class Meta:
        verbose_name_plural = "Me'yoriy hujjatlar"


class Competition(BaseModel):
    title = models.CharField(max_length = 255, verbose_name = "Sarlavha")
    slug = models.SlugField(max_length = 255, unique = True)
    image = models.ImageField(upload_to='competition/images', verbose_name="Rasm")
    description = RichTextUploadingField(verbose_name = "Matn")

    def __str__(self):
        return self.title
    
    def get_url(self):
        return reverse('main:competition_detail', args=[self.slug])
    
    class Meta:
        verbose_name = "Tanlov"
        verbose_name_plural = "Tanlovlar"
        