from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Fight

# Create your views here.

def index(request):

    fights = Fight.objects.all()
    class FightWithShortDescription():
        def __init__(self, fight):
            self.fight = fight
            self.short_description = "%s%s" % (' '.join(fight.description.split(" ")[:7]), "...")            
     
    fights_with_short_description = []

    for fight in fights:
        fights_with_short_description.append(FightWithShortDescription(fight))
    
    template = loader.get_template('FeathersFightApp/index.html')
    context = {
        'fights_list':fights_with_short_description,
    }
    return HttpResponse(template.render(context, request))

def fight(request, fight_id):
    fight = Fight.objects.get(pk=fight_id)
    template = loader.get_template('FeathersFightApp/fight.html')
    context = {
        'fight':fight,
    }
    return HttpResponse(template.render(context, request))