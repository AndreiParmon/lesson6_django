from django.core.management.base import BaseCommand
from myapp2.models import ArticleModel, AuthorModel
from django.utils import lorem_ipsum
from random import choice


class Command(BaseCommand):
    def handle(self, *args, **options):
        authors = AuthorModel.objects.all()
        for i in range(0, 5):
            articles = ArticleModel(author_id=choice(authors),
                                    title=f'Статья #{i}',
                                    text=lorem_ipsum.paragraphs(4),
                                    category=f'Категория {i}',
                                    publication_flag=choice([True, False]))
            articles.save()
            self.stdout.write(f'{articles}')
