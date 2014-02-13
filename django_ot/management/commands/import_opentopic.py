from django.core.management.base import BaseCommand
from django_ot.models import OtConfig


class Command(BaseCommand):

    def handle(self, *args, **options):
        configs = OtConfig.objects.activated()
        for config in configs:
            config.import_news()
