from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        from django_ot.models import OtConfig
        configs = OtConfig.objects.activated()
        for config in configs:
            config.import_news()
