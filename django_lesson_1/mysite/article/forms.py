from django import forms
from article.models import Article


class ArticleForm(forms.ModelForm):
    # title = forms.CharField(required=True)

    class Meta:
        model = Article
        fields = '__all__'
        labels = {
            'title': 'Custom Title',
        }
