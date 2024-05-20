from django.db import models
from shared.models import BaseModel
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class Carousel(BaseModel):
    image = models.ImageField(upload_to='carousel',verbose_name='Rasm')
    content = models.CharField(max_length = 150, null = True, blank = True, verbose_name = _("matn 1"))
    content2 = models.CharField(max_length = 255, null = True, blank = True, verbose_name = _("matn 2"))

    
    class Meta:
        verbose_name = _('Carousel')
        verbose_name_plural = _('Carousels')

class StartUpProjects(BaseModel):
    title = models.CharField(max_length = 150, unique = True, verbose_name = _("sarlavha"))
    slug = models.SlugField(max_length = 150, unique = True)
    image = models.ImageField(upload_to='startup/images', verbose_name=_("Rasm"))
    content = models.TextField(verbose_name = _("Loyiha ta'rifi"))
    is_available = models.BooleanField(default = False, verbose_name = _("mavjudligi"))

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = _("startup project")
        verbose_name_plural = _("startup projects")

class TalentedStudents(BaseModel):
    TYPE = (
        ('PRESIDENT', _("Prezident stipendiatlar")),
        ('STATE', _("Davlat stipendiatlar")),
        ('TALENT', _("Iqtidorli talabalar"))
    )
    first_name = models.CharField(max_length = 150, verbose_name = _("ism"))
    last_name = models.CharField(max_length = 150, verbose_name = _("Familiya"))
    patronymic = models.CharField(max_length = 150, verbose_name = _("Otasining ismi"))
    image = models.ImageField(upload_to='talent-tudent/images', null=True, blank=True, verbose_name=_("Talaba rasmi"))
    teacher_full_name = models.CharField(max_length = 255, verbose_name = _("O'qituvchi F.I.SH"))
    description = models.TextField(null = True, blank = True, verbose_name = _("Talaba haqida ma'lumot"))
    is_available = models.BooleanField(default = False, verbose_name=_("mavjudligi"))
    talent_type = models.CharField(max_length = 15, choices = TYPE, default = 'TALENT', verbose_name=_("iqtidor turi"))

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
    doc_type = models.PositiveSmallIntegerField(choices = DOC_TYPE, verbose_name = _("Hujjat turi"))
    file_name = models.CharField(max_length = 255, verbose_name = _("hujjat nomi"))
    file = models.FileField(upload_to='uploads/doc/files', verbose_name=_("fayl"))
    doc_date = models.DateTimeField(default = timezone.now())

    def __str__(self):
        return self.file_name   
    
    class Meta:
        verbose_name_plural = _("Me'yoriy hujjatlar")


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
        verbose_name = _("Tanlov")
        verbose_name_plural = _("Tanlovlar")
        