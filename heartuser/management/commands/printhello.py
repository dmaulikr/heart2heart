from django.core.management.base import BaseCommand, CommandError
from h2hmainsite.tasks import add
class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            '--name',
            nargs='+',
            type=str,
            help='Prints hello to you'
        )

    def handle(self, *args, **options):
        if options['name']:
            self.stdout.write("Hello %s, thanks for trying this command" % options['name'])
            number = add.delay(4, 5)
            print(number)