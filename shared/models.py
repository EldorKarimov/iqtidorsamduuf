from django.db import models
import uuid

class BaseModel(models.Model):
    id = models.UUIDField(default = uuid.uuid4, primary_key = True, editable = False, unique = True)
    created = models.DateTimeField(auto_now_add = True, verbose_name = "yaratilgan sana")
    updated = models.DateTimeField(auto_now = True, verbose_name = "yangilangan sana")

    class Meta:
        abstract = True