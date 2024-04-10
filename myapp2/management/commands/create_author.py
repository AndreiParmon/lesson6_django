from datetime import datetime

from django.core.management.base import BaseCommand
from django.utils import lorem_ipsum
from myapp2.models import AuthorModel


class Command(BaseCommand):
    def handle(self, *args, **options):
        for i in range(0, 5):
            user = AuthorModel(name=f'Имя_{i}',
                               surname=f'Фамилия_{i}',
                               email=f'author{i}@tut.by',
                               bio=lorem_ipsum.words(10),
                               dob=datetime.now().strftime('%Y-%m-%d'))
            user.save()
            self.stdout.write(f'{user}')
