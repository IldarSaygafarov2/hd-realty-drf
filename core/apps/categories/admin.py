from django.contrib import admin
from unfold import admin as unfold_admin

from . import models


@admin.register(models.Category)
class CategoryAdmin(unfold_admin.ModelAdmin):
    list_display = ["id", "name", "slug", "created_at"]
    list_display_links = ["id", "name"]
    prepopulated_fields = {"slug": ("name",)}
    list_filter = ["created_at"]
