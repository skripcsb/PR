from django.core.management.base import BaseCommand
from myapp.parser import parse_hh

class Command(BaseCommand):
    help = 'Parse jobs from hh.ru'

    def add_arguments(self, parser):
        parser.add_argument('query', type=str)

    def handle(self, *args, **kwargs):
        query = kwargs['query']
        parse_hh(query)
        self.stdout.write(self.style.SUCCESS('Successfully parsed jobs'))