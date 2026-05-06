from django.contrib import admin

from unfold import admin as unfold_admin

from . import models


@admin.register(models.District)
class DistrictAdmin(unfold_admin.ModelAdmin):
    list_display = ["id", "name", "slug", "created_at"]
    list_display_links = ["id", "name"]
    prepopulated_fields = {"slug": ("name",)}
    list_filter = ["created_at"]
