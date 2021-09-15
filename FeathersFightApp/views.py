from django.http.request import HttpRequest, QueryDict
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib import auth
from django.db import IntegrityError

from .models import Fight

# Create your views here.

def index_with_no_page(request):
    return HttpResponseRedirect('/1')

def index_with_page(request, index_page_id):

    username = "User"
    logged_in = 0
    if(request.user.is_authenticated == True):
        username = request.user.username
        logged_in = 1

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
        'index_page_id': index_page_id,
        "username": username,
        "logged_in": logged_in
    }
    return HttpResponse(template.render(context, request))

def fight(request, index_page_id, fight_id):
    fight = Fight.objects.get(pk=fight_id)
    template = loader.get_template('FeathersFightApp/fight.html')
    context = {
        'fight':fight,
    }
    return HttpResponse(template.render(context, request))

def register_page(request):
    template = loader.get_template('FeathersFightApp/register.html')
    return HttpResponse(template.render({}, request))
    
def register_process(request):
    
    if(request.method != "POST"):
        return HttpResponse("Not a post method.")
    
    username = request.POST["username"]
    email = request.POST["email"]
    password = request.POST["password"]
    
    # If user already exists
    try:
        user = User.objects.create_user(username=username, email=email, password=password)
    except IntegrityError:
        return HttpResponse("User already registered.")
    else:
        user.save()
        auth.login(request, user)
        return HttpResponseRedirect('/')

def login_page(request):
    template = loader.get_template('FeathersFightApp/login.html')
    return HttpResponse(template.render({}, request))

def login_process(request):
    
    if(request.method != "POST"):
        return HttpResponse("Not a post method.")
    
    username = request.POST["username"]
    password = request.POST["password"]

    user = auth.authenticate(username=username, password=password)
    
    # User's authentication check
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/')
    else: 
        return HttpResponse("Authetication failed.")

def logout_process(request):
    auth.logout(request)
    return HttpResponseRedirect('/')