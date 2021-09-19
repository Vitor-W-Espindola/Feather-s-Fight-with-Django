from django.contrib import admin

from .models import Article, ArticleRequest, SavedArticle

# Register your models here.
admin.site.register(Article)
admin.site.register(SavedArticle)
admin.site.register(ArticleRequest)
