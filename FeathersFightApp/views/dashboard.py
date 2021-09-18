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

from datetime import *

from bs4 import BeautifulSoup, BeautifulStoneSoup


from FeathersFightApp.models import PublicationRequest, Fight, SavePublication

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
    
    saves = SavePublication.objects.filter(author=request.user)

    class SaveWithShortDescription():
        def __init__(self, save):
            self.id = save.id
            self.title = save.title
            self.short_text = "%s%s" % (' '.join(save.text.split(" ")[:6]), "...")  
            self.last_save = save.last_save

    save_with_short_description = []
    for save in saves:
        save_with_short_description.append(SaveWithShortDescription(save))

    context = { 
        'publication_list':fights_with_short_description,
        "username":request.user.username,
        'requests':requests_with_short_description,
        'saves':save_with_short_description
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

    
    return HttpResponseRedirect("/dashboard")

def new_publication_page(request):
    requests = PublicationRequest.objects.filter(author=request.user)
    if(len(requests) > 0):
        return HttpResponse('You have requests awaiting.')
    else:
        form = PublicationRequestForm()
        return render(request, 'FeathersFightApp/new_publication.html', {'form':form})

def edit_publication_page(request, save_id):
    save = get_object_or_404(SavePublication, id=save_id)
    title = save.title
    form = PublicationRequestForm(instance=save)
    context = {
        'title':title,
        'form':form,
        'save':save
    }
    return render(request, 'FeathersFightApp/edit_publication.html', context)

def save_publication_page(request, save_id):
    save = get_object_or_404(SavePublication, id=save_id)
    title = save.title
    form = PublicationRequestForm(instance=save)
    context = {
        'title':title,
        'form':form,
        'save_id':save_id
    }
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

def new_save(request):
    save = SavePublication.objects.create(
        title=request.POST['title'],
        text=request.POST['text'],
        author=request.user,
        last_save = datetime.now()
    )

    return HttpResponseRedirect('/dashboard/edit/%s' % (save.id))

def new_save_go_to_dashboard(request):

    SavePublication.objects.create(
        title=request.POST['title'],
        text=request.POST['text'],
        author=request.user,
        last_save = datetime.now()
    )

    return HttpResponseRedirect('/dashboard')

def edit_save(request, save_id):
    
    title = request.POST['title']
    text = request.POST['text']
    author = request.user

    save = SavePublication.objects.get(pk=save_id)
    save.title = title
    save.text = text
    save.author = author
    save.last_save = datetime.now()
    save.save()

    return HttpResponseRedirect('/dashboard/edit/%s' % (save.id))

def edit_save_go_to_dashboard(request, save_id):

    title = request.POST['title']
    text = request.POST['text']
    author = request.user

    save = SavePublication.objects.get(pk=save_id)
    save.title = title
    save.text = text
    save.author = author
    save.last_save = datetime.now()

    save.save()
    return HttpResponseRedirect('/dashboard')

def delete_save(request, save_id):
    save = SavePublication.objects.filter(pk=save_id).delete()
    return HttpResponseRedirect('/dashboard')

def submit_new(request):
    title = request.POST['title']
    text = request.POST['text']
    author = request.user
    
    pub = PublicationRequest.objects.create(title=title, text=text, author=author, request_datetime=datetime.now())
    pub.save()

    return HttpResponseRedirect('/dashboard')

def submit_save(request, save_id):
    
    title = request.POST['title']
    text = request.POST['text']
    author = request.user
    
    pub = PublicationRequest.objects.create(title=title, text=text, author=author, request_datetime=datetime.now())
    pub.save()

    save = SavePublication.objects.get(pk=save_id)
    save.delete()

    return HttpResponseRedirect('/dashboard')