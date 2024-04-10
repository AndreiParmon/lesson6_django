from django.urls import path
from . import views
from myapp2.views import index

urlpatterns = [
    path('', index),
    path('blog/<int:author_id>/', views.all_articles, name='all_articles'),
    path('article/<int:article_id>/', views.article_page, name='article_page'),
    path('new_author/', views.new_author, name='new_author'),
    path('new_article/', views.new_article, name='new_article'),
]
