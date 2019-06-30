from django.core.management.base import BaseCommand
from article.models import Article


class Command(BaseCommand):
    help = 'Updates title for a provided article id'

    def add_arguments(self, parser):
        parser.add_argument('article_id', type=int)

    def handle(self, *args, **options):
        article_id = options['article_id']
        if article_id:
            try:
                article = Article.objects.get(id=article_id)
                article.title = "Some new title"
                article.save()
                print('Updated!')
            except Article.DoesNotExist:
                print('Article DoesNotExist !')
