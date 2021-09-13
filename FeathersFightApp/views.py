from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("All fighting styles page.")

def fight(request, fight_id):
    return HttpResponse("A fight page -> %s" % fight_id)