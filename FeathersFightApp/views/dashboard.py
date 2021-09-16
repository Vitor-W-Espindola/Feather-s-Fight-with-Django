from FeathersFightApp.forms import PublicationRequestForm
from django.http.request import HttpRequest, QueryDict
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.contrib import auth
from django.db import IntegrityError
import json

from bs4 import BeautifulSoup, BeautifulStoneSoup


from FeathersFightApp.models import PublicationRequest, EditRequest, DeleteRequest, Fight

def removeTags(html):
    soup = BeautifulSoup(html, "html.parser")
    for data in soup(['style', 'script']):
        data.decompose()
  
    # return data by retrieving the tag content
    return ' '.join(soup.stripped_strings)   


def dashboard(request):
    template = loader.get_template('FeathersFightApp/dashboard.html')

    # If User is authenticated
    if(request.user.is_authenticated == True):
        # If User is an author
        if(len(request.user.groups.filter(name='Authors')) == 0):
            return HttpResponse("Not authorized.")
    else:
        return HttpResponse("Not authorized.")

    fights = Fight.objects.filter(author=request.user)
    class FightWithShortDescription():
        def __init__(self, fight):
                
            self.fight = fight
            self.description_with_tags = removeTags(fight.text)
            self.short_description = "%s%s" % (' '.join(self.description_with_tags.split(" ")[: 6]),  "...")
            print(self.short_description)           
     
    fights_with_short_description = []
    
    for fight in fights:
        fights_with_short_description.append(FightWithShortDescription(fight))
    
    fights_with_edit_request = []
    for index in range(0, EditRequest.objects.count()):
        fights_with_edit_request.append(EditRequest.objects.values_list('publication')[index][0])

    fights_with_delete_request = []
    for index in range(0, DeleteRequest.objects.count()):
        fights_with_delete_request.append(DeleteRequest.objects.values_list('publication')[index][0])
    
    requests = PublicationRequest.objects.filter(author=request.user)
    class RequestWithShortDescription():
        def __init__(self, pub_request):
            self.id = pub_request.id
            self.title = pub_request.title
            self.short_text = "%s%s" % (' '.join(pub_request.text.split(" ")[:6]), "...")  
            self.request_datetime = pub_request.request_datetime   
    
    requests_with_short_description = []
    for pub_request in requests:
        requests_with_short_description.append(RequestWithShortDescription(pub_request))
    
    context = { 
        'publication_list':fights_with_short_description,
        "username":request.user.username,
        'publications_with_edit_request': fights_with_edit_request,
        'publications_with_delete_request': fights_with_delete_request,
        'requests':requests_with_short_description
        }
    return HttpResponse(template.render(context, request))

def fight_preview(request, publication_id):
    
    
    # If User is authenticated
    if(request.user.is_authenticated == True):
        # If User is an author and this publication is yours
        try:
            if(Fight.objects.get(pk=publication_id, author=request.user) == None):
                return HttpResponse("Not found.")
        except:
                return HttpResponse("Not found.")
        
    else:
        return HttpResponse("Not authorized.")

    publication = Fight.objects.get(pk=publication_id)
    
    template = loader.get_template('FeathersFightApp/fight_preview.html')

    context = {
        'publication':publication
    }
    return HttpResponse(template.render(context, request))

def fight_edit(request, publication_id):

    
    publication = None

    # If User is authenticated
    if(request.user.is_authenticated == True):
        # If User is an author and this publication is yours
        try:
            publication = Fight.objects.get(pk=publication_id, author=request.user)
            if(publication == None):
                return HttpResponse("Not found.")
        except:
                return HttpResponse("Not found.")

    fights_with_edit_request = []
    for index in range(0, EditRequest.objects.count()):
        fights_with_edit_request.append(EditRequest.objects.values_list('publication')[index][0])

    fights_with_delete_request = []
    for index in range(0, DeleteRequest.objects.count()):
        fights_with_delete_request.append(DeleteRequest.objects.values_list('publication')[index][0])

    if(publication.id in fights_with_edit_request or publication.id in fights_with_delete_request):
        return HttpResponse("You can't edit this publication while it is in awaiting state.")
    else:
        EditRequest.objects.create(publication=publication)
        return HttpResponseRedirect('/dashboard')

def fight_delete(request, publication_id):
    publication = None

    # If User is authenticated
    if(request.user.is_authenticated == True):
        # If User is an author and this publication is yours
        try:
            publication = Fight.objects.get(pk=publication_id, author=request.user)
            if(publication == None):
                return HttpResponse("Not found.")
        except:
                return HttpResponse("Not found.")

    fights_with_edit_request = []
    for index in range(0, EditRequest.objects.count()):
        fights_with_edit_request.append(EditRequest.objects.values_list('publication')[index][0])

    fights_with_delete_request = []
    for index in range(0, DeleteRequest.objects.count()):
        fights_with_delete_request.append(DeleteRequest.objects.values_list('publication')[index][0])
    
    if(publication.id in fights_with_edit_request or publication.id in fights_with_delete_request):
        return HttpResponse("You can't edit this publication while it is in awaiting state.")
    else:
        q = DeleteRequest.objects.create(publication = publication)
        q.save()
        return HttpResponseRedirect("/dashboard")

def new_publication_page(request):
    form = PublicationRequestForm()
    return render(request, 'FeathersFightApp/new_publication.html', {'form':form})

def edit_publication_page(request, publication_id):
    pub = get_object_or_404(Fight, id=publication_id)
    print(pub.style)
    print(pub.text)
    title = pub.style
    form = PublicationRequestForm(instance=pub)
    context = {
        'title':title,
        'form':form,
        'pub_id':publication_id
    }
    print(form)
    return render(request, 'FeathersFightApp/edit_publication.html', context)

def new_publication_request(request):

    if(request.method != "POST"):
        return HttpResponse("Not a post method.")
    
    title = request.POST["title"]
    text = request.POST["text"]

    PublicationRequest.objects.create(title=title, text=text, author=request.user)

    return HttpResponseRedirect('/dashboard')

def request_preview(request, request_id):
    

    pub_request = PublicationRequest.objects.get(pk=request_id)
    
    template = loader.get_template('FeathersFightApp/request_preview.html')

    context = {
        'request':pub_request
    }
    return HttpResponse(template.render(context, request))