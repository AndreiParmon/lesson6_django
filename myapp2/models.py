from django.db import models
from django.urls import reverse


class AuthorModel(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()
    dob = models.DateTimeField()
    fullname = models.CharField(max_length=200, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.fullname = self.name + ' ' + self.surname
        return super().save(args, kwargs)

    def __str__(self):
        return self.fullname


class ArticleModel(models.Model):
    author_id = models.ForeignKey(AuthorModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=100)
    views_count = models.IntegerField(default=0)
    publication_flag = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('article_page', kwargs={'article_id': self.pk})

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(AuthorModel, on_delete=models.CASCADE)
    article = models.ForeignKey(ArticleModel, on_delete=models.CASCADE)
    text = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    changed_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text
