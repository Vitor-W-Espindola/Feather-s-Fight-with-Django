from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Fight

# Create your views here.

def index(request):
    fights = Fight.objects.all()
    template = loader.get_template('FeathersFightApp/index.html')
    context = {
        'fights_list':fights,
    }
    return HttpResponse(template.render(context, request))

def fight(request, fight_id):
    fight = Fight.objects.get(pk=fight_id)
    template = loader.get_template('FeathersFightApp/fight.html')
    context = {
        'fight':fight,
    }
    return HttpResponse(template.render(context, request))