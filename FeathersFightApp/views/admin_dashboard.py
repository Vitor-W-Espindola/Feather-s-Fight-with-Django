from django import template
from FeathersFightApp.views.dashboard import save_publication_page
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

def admin_dashboard(request):
    
    pub_requests = PublicationRequest.objects.all()
    class PublicationRequestWithShortDescription():
        def __init__(self, pub_request):
            self.pub_request = pub_request
            self.short_description = "%s%s" % (' '.join(removeTags(pub_request.text).split(" ")[: 6]),  "...")
    
    publications_saved_with_short_description = []
    
    for pub_request in pub_requests:
        publications_saved_with_short_description.append(PublicationRequestWithShortDescription(pub_request))
    
    publications = Fight.objects.all()
    class PublicationWithShortDescription():
        def __init__(self, pub):
            self.pub = pub
            self.short_description = "%s%s" % (' '.join(removeTags(pub.text).split(" ")[: 6]),  "...")
    
    publications_with_short_description = []
    
    for pub in publications:
        publications_with_short_description.append(PublicationWithShortDescription(pub))

    template = loader.get_template('FeathersFightApp/admin_dashboard.html')
    context = {
        "publications":publications_with_short_description,
        "pub_requests":publications_saved_with_short_description
    }
    return HttpResponse(template.render(context, request))

def admin_preview_request(request, request_id):
    pub_request = PublicationRequest.objects.get(pk=request_id)
    template = loader.get_template('FeathersFightApp/admin_preview_request.html')
    context = {
        'pub_request':pub_request,
    }
    return HttpResponse(template.render(context, request))

def admin_approve(request, request_id):

    save = PublicationRequest.objects.get(pk=request_id)
    save.delete()

    new_fight = Fight.objects.create(title=save.title, text=save.text, pub_date=datetime.now(), author=save.author)

    return HttpResponseRedirect('/admin_dashboard')

def admin_decline(request, request_id):

    save = PublicationRequest.objects.get(pk=request_id)
    SavePublication.objects.create(title=save.title, text=save.text, author=save.author, last_save=save.request_datetime)
    save.delete()

    return HttpResponseRedirect('/admin_dashboard')

def admin_preview(request, pub_id):
    publication = Fight.objects.get(pk=pub_id)
    template = loader.get_template('FeathersFightApp/admin_preview.html')
    context = {
        'publication':publication,
    }
    return HttpResponse(template.render(context, request))

def admin_delete(request, pub_id):

    pub = Fight.objects.get(pk=pub_id)
    pub.delete()

    return HttpResponseRedirect('/admin_dashboard')

