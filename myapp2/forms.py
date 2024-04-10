from django import forms
from .models import AuthorModel, ArticleModel


class NewAuthor(forms.ModelForm):
    class Meta:
        model = AuthorModel
        fields = ['name', 'surname', 'email', 'bio', 'dob']


class NewArticle(forms.ModelForm):
    class Meta:
        model = ArticleModel
        fields = ['author_id', 'title', 'text', 'category', 'publication_flag']
