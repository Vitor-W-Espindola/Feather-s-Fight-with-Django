# forms.py
from django.forms import ModelForm
from .models import ArticleRequest

class ArticleRequestForm(ModelForm):
    class Meta:
        model = ArticleRequest
        fields = ['text']

