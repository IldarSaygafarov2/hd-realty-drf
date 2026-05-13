from django.core.management.base import BaseCommand
from slugify import slugify

from core.apps.categories.models import RenovationType
from core.project.settings import RENOVATION_TYPES


class Command(BaseCommand):
    def handle(self, *args, **options):
        for item in RENOVATION_TYPES:
            new_renovation_type, created = RenovationType.objects.get_or_create(
                title=item,
                slug=slugify(item),
            )
            if created:
                print(f"added: {new_renovation_type=}")
            else:
                print(f"Got: {new_renovation_type=}")
