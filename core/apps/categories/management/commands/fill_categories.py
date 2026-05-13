from django.core.management.base import BaseCommand
from slugify import slugify

from core.apps.categories.models import Category
from core.project.settings import CATEGORIES_LIST


class Command(BaseCommand):
    def handle(self, *args, **options):
        for category in CATEGORIES_LIST:
            category_slug = slugify(category)
            new_category, created = Category.objects.get_or_create(
                name=category,
                slug=category_slug,
            )
            new_category.save()
            if created:
                print(f"Added: {new_category=}")
            else:
                print(f"Got {new_category=}")
