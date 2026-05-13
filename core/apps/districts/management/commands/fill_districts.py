from django.core.management.base import BaseCommand
from slugify import slugify

from core.apps.districts.models import District
from core.project.settings import DISTRICTS_LIST


class Command(BaseCommand):
    def handle(self, *args, **options):
        for district in DISTRICTS_LIST:
            slug = slugify(district)
            new_district, created = District.objects.get_or_create(
                name=district,
                slug=slug,
            )
            if created:
                print(f"Added {new_district=}")
            else:
                print(f"Got: {new_district=}")
