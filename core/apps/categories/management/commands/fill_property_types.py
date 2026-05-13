from django.core.management.base import BaseCommand
from slugify import slugify

from core.apps.categories.models import PropertyType
from core.project.settings import PROPERTY_TYPES_LIST


class Command(BaseCommand):
    def handle(self, *args, **options):
        for item in PROPERTY_TYPES_LIST:
            property_type, created = PropertyType.objects.get_or_create(
                title=item,
                slug=slugify(item),
            )
            property_type.save()
            if created:
                print(f"Added: {property_type=}")
            else:
                print(f"Got {property_type=}")
