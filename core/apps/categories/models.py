from django.db import models

from core.apps.common.models import BaseModel


class Category(BaseModel):
    name = models.CharField(verbose_name="Название", unique=True, max_length=120)
    slug = models.SlugField(verbose_name="Слаг", unique=True, max_length=140)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["-created_at"]
