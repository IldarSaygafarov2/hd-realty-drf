from django.contrib import admin

from . import models

from unfold import admin as unfold_admin


class AdvertisementCharactersticInline(unfold_admin.TabularInline):
    model = models.AdvertisementCharacterstic
    extra = 1


class AdvertisementImageInline(unfold_admin.TabularInline):
    model = models.AdvertisementImage
    extra = 1


@admin.register(models.Advertisement)
class AdvertisementAdmin(unfold_admin.ModelAdmin):
    inlines = [AdvertisementCharactersticInline, AdvertisementImageInline]
