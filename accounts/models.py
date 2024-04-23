from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    id = models.UUIDField(default = uuid.uuid4, primary_key = True, unique = True, editable = False)
    username = models.CharField(
        max_length = 50, unique = True,
        help_text=_(
            "Majburiy. 150 yoki undan kam belgi. Faqat harflar, raqamlar va @/./+/-/_."
        ),
        error_messages={
            "unique": _("Bunday foydalanuvchi nomiga ega foydalanuvchi allaqachon mavjud."),
        },
    )
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    patronymic = models.CharField(max_length = 100, null = True, blank = True)
    phone = models.CharField(max_length = 13, null = True, blank = True)
    image = models.ImageField(upload_to='users/image', null = True, blank = True)
    direction = models.CharField(max_length = 150, null = True, blank = True)
    group = models.CharField(max_length = 150, null = True, blank = True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')