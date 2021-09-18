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

from FeathersFightApp.models import PublicationRequest, EditRequest, DeleteRequest, Fight, SavePublication

def removeTags(html):
    soup = BeautifulSoup(html, "html.parser")
    for data in soup(['style', 'script']):
        data.decompose()
  
    # return data by retrieving the tag content
    return ' '.join(soup.stripped_strings)   

def admin_dashboard(request):
    
    publications_saved = PublicationRequest.objects.all()
    print(publications_saved)
    template = loader.get_template('FeathersFightApp/admin_dashboard.html')

    class SavedPublicationWithShortDescription():
        def __init__(self, save):
            self.save = save
            self.short_description = "%s%s" % (' '.join(removeTags(save.text).split(" ")[: 6]),  "...")
    
    publications_saved_with_short_description = []
    
    for save in publications_saved:
        publications_saved_with_short_description.append(SavedPublicationWithShortDescription(save))
    
    print(publications_saved_with_short_description)
    context = {
        "publications_saved":publications_saved_with_short_description
    }
    return HttpResponse(template.render(context, request))

def admin_preview(request, request_id):
    save = PublicationRequest.objects.get(pk=request_id)
    template = loader.get_template('FeathersFightApp/admin_preview.html')
    context = {
        'save':save,
    }
    return HttpResponse(template.render(context, request))

def admin_approve(request, request_id):

    save = PublicationRequest.objects.get(pk=request_id)
    save.delete()

    new_fight = Fight.objects.create(style=save.title, text=save.text, pub_date=datetime.now(), author=save.author)

    return HttpResponseRedirect('/admin_dashboard')

def admin_decline(request, request_id):

    save = PublicationRequest.objects.get(pk=request_id)
    save.delete()

    return HttpResponseRedirect('/admin_dashboard')