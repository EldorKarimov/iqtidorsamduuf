from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    id = models.UUIDField(default = uuid.uuid4, primary_key = True, unique = True, editable = False)
    username = models.CharField(
        max_length = 50, unique = True,
        help_text=_(
            _("Mandatory. 150 characters or less. Only letters, numbers and @/./+/-/_.")
        ),
        error_messages={
            "unique": _("A user with this username already exists."),
        },
    )
    first_name = models.CharField(max_length = 100, verbose_name=_("first name"))
    last_name = models.CharField(max_length = 100, verbose_name=_("last name"))
    patronymic = models.CharField(max_length = 100, verbose_name=_("patronymic"), null = True, blank = True)
    phone = models.CharField(max_length = 13, verbose_name=_("phone"), null = True, blank = True)
    image_url = models.URLField(null=True, blank=True, verbose_name=_("image link"))
    direction = models.CharField(max_length = 150, verbose_name=_("direction"), null = True, blank = True)
    group = models.CharField(max_length = 150, verbose_name=_("group"), null = True, blank = True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')