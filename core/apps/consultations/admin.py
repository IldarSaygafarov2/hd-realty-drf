from django.contrib import admin

from unfold import admin as unfold_admin
from . import models


@admin.register(models.ConsultationRequest)
class ConsulationRequestAdmin(unfold_admin.ModelAdmin):
    list_display = ["id", "name", "phone"]


@admin.register(models.ContactRequest)
class ContactRequestAdmin(unfold_admin.ModelAdmin):
    pass


@admin.register(models.NextStepRequest)
class NextStepRequestAdmin(unfold_admin.ModelAdmin):
    pass
