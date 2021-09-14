from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator

from .models import Fight

# Create your views here.

def index_with_no_page(request):
    return HttpResponseRedirect('/1')

def index_with_page(request, index_page_id):

    fights = Fight.objects.all()
    
    class FightWithShortDescription():
        def __init__(self, fight):
            self.fight = fight
            self.short_description = "%s%s" % (' '.join(fight.description.split(" ")[:6]), "...")            
     
    fights_with_short_description = []
    
    for fight in fights:
        fights_with_short_description.append(FightWithShortDescription(fight))
    
    items_for_page = 4
    paginator = Paginator(fights_with_short_description, items_for_page)

    template = loader.get_template('FeathersFightApp/index.html')
    context = {
        'fights_list': paginator.page(index_page_id).object_list,
        'range_of_pages': paginator.page_range,
        'index_page_id': index_page_id
    }
    return HttpResponse(template.render(context, request))

def fight(request, index_page_id, fight_id):
    fight = Fight.objects.get(pk=fight_id)
    template = loader.get_template('FeathersFightApp/fight.html')
    context = {
        'fight':fight,
    }
    return HttpResponse(template.render(context, request))

def register(request):
    template = loader.get_template('FeathersFightApp/register.html')
    return HttpResponse(template.render({}, request))