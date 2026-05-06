from django.db import models

from core.apps.common.models import BaseModel


class District(BaseModel):
    name = models.CharField(verbose_name="Название", unique=True, max_length=120)
    slug = models.SlugField(verbose_name="Слаг", unique=True, max_length=140)

    def __str__(self):
        return self.name + "1"

    class Meta:
        verbose_name = "Район"
        verbose_name_plural = "Районы"
        ordering = ["-created_at"]
