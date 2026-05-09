from django.contrib import admin
from unfold import admin as unfold_admin


from . import models


@admin.register(models.FAQ)
class FAQAdmin(unfold_admin.ModelAdmin):
    pass


class PortfolioJobInline(unfold_admin.TabularInline):
    model = models.PortfolioJob
    extra = 1


class PortfolioImageInline(unfold_admin.TabularInline):
    model = models.PortfolioImage
    extra = 1


@admin.register(models.Portfolio)
class PortfolioAdmin(unfold_admin.ModelAdmin):
    inlines = [PortfolioJobInline, PortfolioImageInline]


class ServiceIncludeInline(unfold_admin.TabularInline):
    model = models.ServiceInclude
    extra = 1


@admin.register(models.Service)
class ServiceAdmin(unfold_admin.ModelAdmin):
    inlines = [ServiceIncludeInline]
