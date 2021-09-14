from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

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
    
    number_of_pages = range(1, fights.count()//4 + 2)
    page_interval_start = 4*(index_page_id - 1)
    page_interval_end = (4*(index_page_id - 1) + 4)
    print(page_interval_start)
    print(page_interval_end)
    print(number_of_pages)

    for fight in fights[page_interval_start:page_interval_end]:
        fights_with_short_description.append(FightWithShortDescription(fight))
    
    template = loader.get_template('FeathersFightApp/index.html')
    context = {
        'fights_list':fights_with_short_description,
        'number_of_pages':number_of_pages,
        'index_page_id':index_page_id
    }
    return HttpResponse(template.render(context, request))

def fight(request, index_page_id, fight_id):
    fight = Fight.objects.get(pk=fight_id)
    template = loader.get_template('FeathersFightApp/fight.html')
    context = {
        'fight':fight,
    }
    return HttpResponse(template.render(context, request))