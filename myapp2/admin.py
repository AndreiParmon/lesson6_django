from django.contrib import admin

from .models import AuthorModel, ArticleModel, Comment


@admin.register(ArticleModel)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['author_id', 'title', 'category']
    readonly_fields = ['publication_date', 'views_count']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['author_id'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Текст статьи',
                'fields': ['title', 'text'],
            },
        ),
        (
            'Дата публикации и категория',
            {
                'fields': ['category', 'publication_date'],
            }
        ),
        (
            'Число просмотров и статус',
            {
                'description': 'Количество просмотров',
                'fields': ['views_count', 'publication_flag'],
            }
        ),
    ]


@admin.register(AuthorModel)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'dob', 'email']
    readonly_fields = ['dob']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['fullname'],
            },
        ),
        (
            'Биография автора',
            {
                'classes': ['collapse'],
                'description': 'Биография',
                'fields': ['dob', 'bio'],
            },
        ),
        (
            'Контакты',
            {
                'description': 'Контактная информация',
                'fields': ['email'],
            }
        ),
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'article', 'text', 'publication_date', 'changed_date']
    readonly_fields = ['publication_date', 'changed_date']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['author'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Комментарий',
                'fields': ['article', 'text'],
            },
        ),
        (
            'Дата публикации и изменения',
            {
                'fields': ['publication_date', 'changed_date'],
            }
        ),
    ]
