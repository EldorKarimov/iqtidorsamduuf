from django.db import models
from shared.models import BaseModel
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class Carousel(BaseModel):
    image = models.ImageField(upload_to='carousel',verbose_name= _('Image'))
    content = models.CharField(max_length = 150, null = True, blank = True, verbose_name = _("content 1"))
    content2 = models.CharField(max_length = 255, null = True, blank = True, verbose_name = _("content 2"))

    
    class Meta:
        verbose_name = _('Carousel')
        verbose_name_plural = _('Carousels')

class StartUpProjects(BaseModel):
    title = models.CharField(max_length = 150, unique = True, verbose_name = _("title"))
    slug = models.SlugField(max_length = 150, unique = True)
    image = models.ImageField(upload_to='startup/images', verbose_name=_("image"))
    content = models.TextField(verbose_name = _("Loyiha ta'rifi"))
    is_available = models.BooleanField(default = False, verbose_name = _("is available"))

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = _("startup project")
        verbose_name_plural = _("startup projects")

class TalentedStudents(BaseModel):
    TYPE = (
        ('PRESIDENT', _("presidential stipendium holers")),
        ('STATE', _("Davlat stipendiatlar")),
        ('TALENT', _("talent students"))
    )
    first_name = models.CharField(max_length = 150, verbose_name = _("first name"))
    last_name = models.CharField(max_length = 150, verbose_name = _("last name"))
    patronymic = models.CharField(max_length = 150, verbose_name = _("patronymic"))
    image = models.ImageField(upload_to='talent-tudent/images', null=True, blank=True, verbose_name=_("student image"))
    teacher_full_name = models.CharField(max_length = 255, verbose_name = _("teacher full name"))
    description = models.TextField(null = True, blank = True, verbose_name = _("student description"))
    is_available = models.BooleanField(default = False, verbose_name=_("is available"))
    talent_type = models.CharField(max_length = 15, choices = TYPE, default = 'TALENT', verbose_name=_("talent type"))

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name = _("Talent student")
        verbose_name_plural = _("talent students")

class Documents(BaseModel):
    DOC_TYPE = (
        (1, _("Buyruqlar")),
        (2, _("Nizomlar")),
    )
    doc_type = models.PositiveSmallIntegerField(choices = DOC_TYPE, verbose_name = _("document type"))
    file_name = models.CharField(max_length = 255, verbose_name = _("file name"))
    file = models.FileField(upload_to='uploads/doc/files', verbose_name=_("file"))
    doc_date = models.DateTimeField(default = timezone.now())

    def __str__(self):
        return self.file_name   
    
    class Meta:
        verbose_name_plural = _("Regulatory documents")


class Competition(BaseModel):
    title = models.CharField(max_length = 255, verbose_name = _("title"))
    slug = models.SlugField(max_length = 255, unique = True)
    image = models.ImageField(upload_to='competition/images', verbose_name=_("image"))
    description = RichTextUploadingField(verbose_name = _("desctiption"))

    def __str__(self):
        return self.title
    
    def get_url(self):
        return reverse('main:competition_detail', args=[self.slug])
    
    class Meta:
        verbose_name = _("Competition")
        verbose_name_plural = _("Competitions")
        