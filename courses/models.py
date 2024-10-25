from django.db import models
from shared.models import BaseModel
from accounts.models import CustomUser
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator

class Author(BaseModel):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio = RichTextUploadingField()

    def __str__(self):
        return self.user.get_full_name()
    
class Course(BaseModel):
    COURSE_TYPE = (
        ("online", "Online"),
        ("offline", "Offline"),
    )
    title = models.CharField(max_length=150, unique=True, verbose_name=_("title"))
    slug = models.SlugField(max_length=150, unique=True)
    content = RichTextUploadingField(verbose_name=_("content"))
    youtube_link = models.CharField(max_length=255, null=True, blank=True, verbose_name=_("youtube link"))
    course_type = models.CharField(max_length=8, choices=COURSE_TYPE, verbose_name=_("course type"))
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, verbose_name=_("author"))
    file = models.FileField(
    upload_to='uploads/course/files',
    null=True,
    blank=True,
    verbose_name=_("Fayl"),
    validators=[FileExtensionValidator(['pdf', 'doc', 'docx', 'ppt', 'pptx'])]
    )

    def __str__(self):
        return self.title