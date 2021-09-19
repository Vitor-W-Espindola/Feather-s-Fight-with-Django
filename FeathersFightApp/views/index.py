from django.http.response import HttpResponseRedirect
from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator

from bs4 import BeautifulSoup

from FeathersFightApp.models import Article

# This method is used to remove all html tags in the text
def removeTags(html):

    soup = BeautifulSoup(html, "html.parser")

    for data in soup(['style', 'script']):
        data.decompose()
  
    return ' '.join(soup.stripped_strings)   

# This method is used when user browse localhost:8000/
def index_with_no_page(request):
    return HttpResponseRedirect('/1')

# This method is used to retrieve the home page
# and display the current page of articles
# from the url localhost:8000/{page}
def index_with_page(request, index_page_id):

    username = "Visitor"
    logged_in = 0
    author = 0
    admin = 0

    if(request.user.is_authenticated == True):
        username = request.user.username
        logged_in = 1
        # If User is an author
        if(len(request.user.groups.filter(name='Authors')) != 0):
            author = 1
        if(request.user.is_superuser):
            admin = 1

    articles = Article.objects.all()

    # This class is used to retrieve the article with its short description
    class ArticlesWithShortDescription():
        def __init__(self, article): 
            self.article = article
            self.description_with_tags = removeTags(article.text)
            self.short_description = "%s%s" % (' '.join(self.description_with_tags.split(" ")[: 6]),  "...")

    articles_with_short_description = []
    
    for article in articles:
        articles_with_short_description.append(ArticlesWithShortDescription(article))

    items_for_page = 4
    paginator = Paginator(articles_with_short_description, items_for_page)

    template = loader.get_template('FeathersFightApp/index.html')
    context = {
        'articles_list': paginator.page(index_page_id).object_list,
        'range_of_pages': paginator.page_range,
        'index_page_id': index_page_id,
        "username": username,
        "logged_in": logged_in,
        "author": author,
        "admin": admin
    }

    return HttpResponse(template.render(context, request))

# This method is used to retrieve the article page
# by the url localhost:8000/{page}/article/{article_id}
def article(request, article_id):

    article = Article.objects.get(pk=article_id)

    template = loader.get_template('FeathersFightApp/article.html')
    context = {
        'article':article,
    }

    return HttpResponse(template.render(context, request))
