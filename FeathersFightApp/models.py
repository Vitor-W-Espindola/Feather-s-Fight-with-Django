from django.db import models
from django.contrib.auth.models import User
from datetime import *

from ckeditor.fields import RichTextField
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=30)
    text = RichTextField()
    pub_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, limit_choices_to={'groups__name':'Authors'})

    def __str__(self):
        return "%i -> %s" % (self.id, self.title)

class ArticleRequest(models.Model):
    title = models.CharField(max_length=30)
    text = RichTextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False, limit_choices_to={'groups__name':'Authors'})
    request_datetime = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return "%s - %s" % (self.title, self.author.username)
class SavedArticle(models.Model):
    title = models.CharField(max_length=30)
    text = RichTextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False, limit_choices_to={'groups__name':'Authors'})
    last_save = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return "%s - %s" % (self.title, self.author.username)
