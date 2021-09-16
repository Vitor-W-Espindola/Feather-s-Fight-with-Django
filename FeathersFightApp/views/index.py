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


def index_with_no_page(request):
    return HttpResponseRedirect('/1')

def index_with_page(request, index_page_id):

    username = "User"
    logged_in = 0
    author = 0
    if(request.user.is_authenticated == True):
        username = request.user.username
        logged_in = 1
        # If User is an author
        if(len(request.user.groups.filter(name='Authors')) != 0):
            author = 1

    fights = Fight.objects.all()

    fights_with_edit_request = []
    for index in range(0, EditRequest.objects.count()):
        fights_with_edit_request.append(EditRequest.objects.values_list('publication')[index][0])

    fights_with_delete_request = []
    for index in range(0, DeleteRequest.objects.count()):
        fights_with_delete_request.append(DeleteRequest.objects.values_list('publication')[index][0])



    class FightWithShortDescription():
        
        
        def __init__(self, fight):
                
            self.fight = fight
            self.description_with_tags = removeTags(fight.text)
            self.short_description = "%s%s" % (' '.join(self.description_with_tags.split(" ")[: 6]),  "...")
            print(self.short_description)

    

    fights_with_short_description = []
    
    for fight in fights:
        if(fight.id not in fights_with_edit_request and fight.id not in fights_with_delete_request):
            fights_with_short_description.append(FightWithShortDescription(fight))
        else:
            print("%s This fight has a edit or delete request." % (fight.style))

    items_for_page = 4
    paginator = Paginator(fights_with_short_description, items_for_page)

    template = loader.get_template('FeathersFightApp/index.html')
    context = {
        'fights_list': paginator.page(index_page_id).object_list,
        'range_of_pages': paginator.page_range,
        'index_page_id': index_page_id,
        "username": username,
        "logged_in": logged_in,
        "author": author
    }
    return HttpResponse(template.render(context, request))

def fight(request, fight_id):
    fight = Fight.objects.get(pk=fight_id)
    template = loader.get_template('FeathersFightApp/fight.html')
    context = {
        'fight':fight,
    }
    return HttpResponse(template.render(context, request))
