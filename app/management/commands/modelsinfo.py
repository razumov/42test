from django.core.management.base import BaseCommand
from django.db import models


class Command(BaseCommand):
    help = 'Shows models info'

    def handle(self, *args, **options):
        my_models = models.get_models()
        self.stdout.write('Total models count: %d\n' % len(my_models))
        self.stderr.write('error: Total models count: %d\n' % len(my_models))
        for my_model in my_models:
            self.stdout.write('%s contains %d objects\n' % \
                              (str(my_model), my_model.objects.count()))
            self.stderr.write('error: %s contains %d objects\n' % \
                              (str(my_model), my_model.objects.count()))