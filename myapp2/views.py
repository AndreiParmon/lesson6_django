from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404

from .models import ArticleModel, Comment
from .forms import NewAuthor, NewArticle


def index(request):
    return render(request, 'myapp2/index.html')


def all_articles(request: HttpRequest, author_id):
    articles = ArticleModel.objects.filter(author_id=author_id)
    return render(request, 'myapp2/blog.html', {'articles': articles})


def article_page(request: HttpRequest, article_id):
    article = get_object_or_404(ArticleModel, pk=article_id)
    article.views_count += 1
    article.save()
    # comments = Comment.object.filter(post=article)
    return render(request, 'myapp2/article.html', {'article': article})


def new_author(request):
    if request.method == 'POST':
        form = NewAuthor(request.POST)
        if form.is_valid():
            # author = Author.objects.create(
            #     first_name=data['first_name'],
            #     last_name=data['last_name'],
            #     email=data['email'],
            #     bio=data['bio'],
            #     birth_date=data['birth_date']
            # )
            author = form.save()
            return all_articles(request, author.pk)
        else:
            return render(request, 'myapp2/new_author.html', {'form': form})
    return render(request, 'myapp2/new_author.html', {'form': NewAuthor})


def new_article(request):
    if request.method == 'POST':
        form = NewArticle(request.POST)
        if form.is_valid():
            article = form.save()
            return article_page(request, article.pk)
        else:
            return render(request, 'myapp2/new_article.html', {'form': form})
    return render(request, 'myapp2/new_article.html', {'form': NewArticle})
