from FeathersFightApp.forms import ArticleRequestForm
from django.http.request import HttpRequest
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User

from datetime import *

from bs4 import BeautifulSoup

from FeathersFightApp.models import Article, ArticleRequest, SavedArticle

# This method is used to remove all html tags in the text
def removeTags(html):
    soup = BeautifulSoup(html, "html.parser")
    for data in soup(['style', 'script']):
        data.decompose()
  
    return ' '.join(soup.stripped_strings)   

# This method is used to retrieve the author dashboard
# when the url localhost:8000/dashboard is required
def dashboard(request):

    # If User is authenticated
    if(request.user.is_authenticated == True):
        # If User is an author
        if(len(request.user.groups.filter(name='Authors')) == 0):
            return HttpResponse("Not authorized.")
    else:
        return HttpResponse("Not authorized.")

    # Retrieve all author's articles
    articles = Article.objects.filter(author=request.user)

    # This class is used to retrieve the article with its short description
    class ArticleWithShortDescription():
        def __init__(self, article):
                
            self.article = article
            self.description_with_tags = removeTags(article.text)
            self.short_description = "%s%s" % (' '.join(self.description_with_tags.split(" ")[: 6]),  "...")
     
    articles_with_short_description = []

    for article in articles:
        articles_with_short_description.append(ArticleWithShortDescription(article))
    
    # Retrieve all author's article requests
    article_requests = ArticleRequest.objects.filter(author=request.user)

    # This class is used to retrieve the publication request with its short description
    class ArticleRequestWithShortDescription():
        def __init__(self, pub_request):
            self.id = pub_request.id
            self.title = pub_request.title
            self.short_text = "%s%s" % (' '.join(pub_request.text.split(" ")[:6]), "...")  
            self.request_datetime = pub_request.request_datetime   
    
    article_requests_with_short_description = []

    for article_request in article_requests:
        article_requests_with_short_description.append(ArticleRequestWithShortDescription(article_request))
    
    # Retrieve all author's saved publications
    saved_articles = SavedArticle.objects.filter(author=request.user)

    # This class is used to retrieve the saved publication with its short description
    class SavedArticleWithShortDescription():
        def __init__(self, save):
            self.id = save.id
            self.title = save.title
            self.short_text = "%s%s" % (' '.join(save.text.split(" ")[:6]), "...")  
            self.last_save = save.last_save

    saved_article_with_short_description = []
    for saved_article in saved_articles:
        saved_article_with_short_description.append(SavedArticleWithShortDescription(saved_article))

    template = loader.get_template('FeathersFightApp/dashboard.html')
    context = { 
        'article_list':articles_with_short_description,
        'article_requests':article_requests_with_short_description,
        'saved_articles':saved_article_with_short_description,
        'username':request.user.username,
        }

    return HttpResponse(template.render(context, request))

# This method is used to retrieve a preview of author's article
# when the url localhost:8000/dashboard/article_preview/{article_id}/
def article_preview(request, article_id):
     
    # If User is authenticated
    if(request.user.is_authenticated == True):
        # If User is an author and this article is yours
        try:
            if(Article.objects.get(pk=article_id, author=request.user) == None):
                return HttpResponse("Not found.")
        except:
                return HttpResponse("Not found.")
        
    else:
        return HttpResponse("Not authorized.")

    article = Article.objects.get(pk=article_id)
    
    template = loader.get_template('FeathersFightApp/article_preview.html')

    context = {
        'article':article
    }
    return HttpResponse(template.render(context, request))

# This method is used to retrieve the new article page
# when the url localhost:8000/dashboard/new
def new_article_page(request):
    form = ArticleRequestForm()
    return render(request, 'FeathersFightApp/new_article.html', {'form':form})

# This method is used to create a new article request
# when the url localhost:8000/dashboard/new/submit is required
def new_article_request(request):

    if(request.method != "POST"):
        return HttpResponse("Not a post method.")

    requests = ArticleRequest.objects.filter(author=request.user)
    if(len(requests) > 0):
        return HttpResponse('You have requests awaiting.')
    else:

        title = request.POST["title"]
        text = request.POST["text"]
        author = request.user

        article_request = ArticleRequest.objects.create(
            title=title,
             text=text,
              author=author,
              request_datetime = datetime.now())

        article_request.save()

        return HttpResponseRedirect('/dashboard')


# This method is used to create a new article save
# and redirect to edit article page
# when the url localhost:8000/dashboard/new/save/ is required
def new_article_save_and_keep_writing(request):
    
    if(request.user.is_authenticated == True):
        title=request.POST['title']
        text=request.POST['text']
        author=request.user
        last_save = datetime.now()

        saved_article = SavedArticle.objects.create(
            title=title,
             text=text,
              author=author,
              last_save = last_save
        )
        saved_article.save()

        return HttpResponseRedirect('/dashboard/edit/%i' % saved_article.id)
    else:
        return HttpResponse('')


# This method is used to create a new article save
# and go back to dashboard
# when the url localhost:8000/dashboard/new/save/dashboard is required
def new_article_save_and_go_to_dashboard(request):

    SavedArticle.objects.create(
        title=request.POST['title'],
        text=request.POST['text'],
        author=request.user,
        last_save = datetime.now()
    )

    return HttpResponseRedirect('/dashboard')

# This method is used to edit an article save
# when the url localhost:8000/dashboard/edit/{{ int:save_id }}
def edit_save(request, article_save_id):
    
    article_save = None

    # If User is authenticated
    if(request.user.is_authenticated == True):
        # If User is an author and this publication is yours
        try:
            article_save = SavedArticle.objects.get(pk=article_save_id, author=request.user)
            if(article_save == None):
                return HttpResponse("Not found.")
        except:
                return HttpResponse("Not found.")
    
    form = ArticleRequestForm(instance=article_save)

    template = loader.get_template('FeathersFightApp/edit_save.html')
    context = {
        'form':form,
        'article_save':article_save
    }

    return HttpResponse(template.render(context, request))

# This method is used to submit an article save
# and go back to dashboard
# when the url localhost:8000/dashboard/edit/submit/{{ save_id }}
def edit_save_submit(request, article_save_id):
        
    article_requests = ArticleRequest.objects.filter(author=request.user)
    if(len(article_requests) > 0):
        return HttpResponse('You have requests awaiting.')
    else:
        title = request.POST['title']
        text = request.POST['text']
        author = request.user
        
        pub = ArticleRequest.objects.create(title=title, text=text, author=author, request_datetime=datetime.now())
        pub.save()

        save = SavedArticle.objects.get(pk=article_save_id)
        save.delete()

        return HttpResponseRedirect('/dashboard')

# This method is used to edit an article save and 
# redirect to edit article page, retrieving its own saved data
# when the url localhost:8000/dashboard/edit/save/{{ int:save_id }}
def edit_save_save_and_keep_writing(request, article_save_id):
    
    title = request.POST['title']
    text = request.POST['text']
    author = request.user

    article_save = SavedArticle.objects.get(pk=article_save_id)
    article_save.title = title
    article_save.text = text
    article_save.author = author
    article_save.last_save = datetime.now()
    article_save.save()

    return HttpResponseRedirect('/dashboard/edit/%s' % (article_save.id))

# This method is used to edit an article save
# and go back to dashboard
# when the url localhost:8000/dashboard/edit/save/dashboard/{{ save_id }}
def edit_save_save_and_go_to_dashboard(request, article_save_id):

    title = request.POST['title']
    text = request.POST['text']
    author = request.user

    article_save = SavedArticle.objects.get(pk=article_save_id)
    article_save.title = title
    article_save.text = text
    article_save.author = author
    article_save.last_save = datetime.now()
    article_save.save()

    return HttpResponseRedirect('/dashboard')

# This method is used to delete an article save
# and go back to dashboard
# when the url localhost:8000/dashboard/delete/save/{{ save_id }}
def delete_save(request, article_save_id):
    save = SavedArticle.objects.filter(pk=article_save_id).delete()
    return HttpResponseRedirect('/dashboard')

# This method is used to retrieve
# the article request preview 
# when the url localhost:8000/dashboard/article_request_preview/{{ article_request_id }}
def article_request_preview(request, article_request_id):

    article_request = ArticleRequest.objects.get(pk=article_request_id)
    
    template = loader.get_template('FeathersFightApp/article_request_preview.html')

    context = {
        'article_request':article_request
    }
    return HttpResponse(template.render(context, request))