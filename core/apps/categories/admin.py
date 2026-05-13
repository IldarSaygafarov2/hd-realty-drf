from django.contrib import admin
from unfold import admin as unfold_admin

from . import models


@admin.register(models.Category)
class CategoryAdmin(unfold_admin.ModelAdmin):
    list_display = ["id", "name", "slug", "created_at"]
    list_display_links = ["id", "name"]
    prepopulated_fields = {"slug": ("name",)}
    list_filter = ["created_at"]


@admin.register(models.RenovationType)
class RenovationTypeAdmin(unfold_admin.ModelAdmin):
    list_display = ["title", "slug", "created_at", "updated_at"]
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ["created_at"]
    search_fields = ["title"]


@admin.register(models.PropertyType)
class PropertyTypeAdmin(unfold_admin.ModelAdmin):
    list_display = ["title", "slug", "created_at", "updated_at"]
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ["created_at"]
    search_fields = ["title"]
