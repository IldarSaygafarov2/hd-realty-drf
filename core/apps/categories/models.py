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


class RenovationType(BaseModel):
    title = models.CharField(verbose_name="Название", max_length=50, unique=True)
    slug = models.SlugField(verbose_name="Слаг", max_length=60, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Тип ремонта"
        verbose_name_plural = "Типы ремонта"
        ordering = ["-created_at"]


class PropertyType(BaseModel):
    title = models.CharField(verbose_name="Название", max_length=100, unique=True)
    slug = models.SlugField(verbose_name="Слаг", max_length=120, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Тип недвижимости"
        verbose_name_plural = "Типы недвижимости"
        ordering = ["-created_at"]
