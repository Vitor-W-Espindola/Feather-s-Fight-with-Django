from FeathersFightApp.views.index import article
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader

from datetime import *

from bs4 import BeautifulSoup

from FeathersFightApp.models import Article, ArticleRequest, SavedArticle

#  This method is used to remove all html tags in the tex
def removeTags(html):
    soup = BeautifulSoup(html, "html.parser")
    for data in soup(['style', 'script']):
        data.decompose()
  
    return ' '.join(soup.stripped_strings)   

# This method is used to retrieve the admin dashboard
# when the url localhost:8000/dashboard is required
def admin_dashboard(request):
    
    article_requests = ArticleRequest.objects.all()
    class ArticleRequestWithShortDescription():
        def __init__(self, article_request):
            self.article_request = article_request
            self.short_description = "%s%s" % (' '.join(removeTags(article_request.text).split(" ")[: 6]),  "...")
    
    article_requests_with_short_description = []
    
    for article_request in article_requests:
        article_requests_with_short_description.append(ArticleRequestWithShortDescription(article_request))
    
    articles = Article.objects.all()
    class ArticleWithShortDescription():
        def __init__(self, article):
            self.article = article
            self.short_description = "%s%s" % (' '.join(removeTags(article.text).split(" ")[: 6]),  "...")
    
    articles_with_short_description = []
    
    for article in articles:
        articles_with_short_description.append(ArticleWithShortDescription(article))

    template = loader.get_template('FeathersFightApp/admin_dashboard.html')
    context = {
        "articles":articles_with_short_description,
        "article_requests":article_requests_with_short_description
    }
    
    return HttpResponse(template.render(context, request))

# This method is used to retrieve the preview of an article request
# when the url localhost:8000/admin_dashboard/admin_article_request_preview/{{ article_request_id }} is required
def admin_article_request_preview(request, article_request_id):
    article_request = ArticleRequest.objects.get(pk=article_request_id)
    template = loader.get_template('FeathersFightApp/admin_article_request_preview.html')
    context = {
        'article_request':article_request,
    }
    return HttpResponse(template.render(context, request))

# This method is used to retrieve the preview of an article
# when the url localhost:8000/admin_dashboard/admin_article_preview/{{ article_id }} is required
def admin_article_preview(request, article_id):
    publication = Article.objects.get(pk=article_id)
    template = loader.get_template('FeathersFightApp/admin_article_preview.html')
    context = {
        'publication':publication,
    }
    return HttpResponse(template.render(context, request))

# This method is used to approve an article request 
# and redirect to admin dashboard
# when the url localhost:8000/admin_dashboard/approve/{{ article_request_id }} is required
def admin_approve(request, article_request_id):

    article_request = ArticleRequest.objects.get(pk=article_request_id)
    article_request.delete()

    new_fight = Article.objects.create(
        title=article_request.title,
         text=article_request.text,
          pub_date=datetime.now(),
           author=article_request.author)

    return HttpResponseRedirect('/admin_dashboard')

# This method is used to decline an article request,
# return the article request to author as a saved article 
# and redirect to admin dashboard
# when the url localhost:8000/admin_dashboard/decline/{{ article_request_id }} is required
def admin_decline(request, article_request_id):

    article_request = ArticleRequest.objects.get(pk=article_request_id)
    SavedArticle.objects.create(
        title=article_request.title,
         text=article_request.text,
          author=article_request.author,
           last_save=article_request.request_datetime)
    article_request.delete()

    return HttpResponseRedirect('/admin_dashboard')

# This method is used to delete an article,
# and redirect to admin dashboard
# when the url localhost:8000/admin_dashboard/delete/{{ article_id }} is required
def admin_delete(request, article_id):

    article = Article.objects.get(pk=article_id)
    article.delete()

    return HttpResponseRedirect('/admin_dashboard')

