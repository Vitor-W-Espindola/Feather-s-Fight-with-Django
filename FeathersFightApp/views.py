from django.http.request import HttpRequest, QueryDict
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.contrib import auth
from django.db import IntegrityError
import json

from .models import PublicationRequest, EditRequest, DeleteRequest, Fight
from .forms import QuillFieldForm

# Create your views here.

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
    print(fights_with_edit_request)
    print(fights_with_delete_request)

    class FightWithShortDescription():
        def __init__(self, fight):
            self.fight = fight
            self.short_description = "%s%s" % (' '.join(fight.description.split(" ")[:6]), "...")            
    
    fights_with_short_description = []
    
    for fight in fights:
        if(fight.id not in fights_with_edit_request and fight.id not in fights_with_delete_request):
            print(fight.id)
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
    except ValueError:
        return HttpResponse("Fill all form fields.")
        
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
            self.short_description = "%s%s" % (' '.join(fight.description.split(" ")[:6]), "...")            
     
    fights_with_short_description = []
    
    for fight in fights:
        fights_with_short_description.append(FightWithShortDescription(fight))
    
    fights_with_edit_request = []
    for index in range(0, EditRequest.objects.count()):
        fights_with_edit_request.append(EditRequest.objects.values_list('publication')[index][0])

    fights_with_delete_request = []
    for index in range(0, DeleteRequest.objects.count()):
        fights_with_delete_request.append(DeleteRequest.objects.values_list('publication')[index][0])
    
    context = { 
        'publication_list':fights_with_short_description,
        "username":request.user.username,
        'publications_with_edit_request': fights_with_edit_request,
        'publications_with_delete_request': fights_with_delete_request
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

    fights_with_edit_request = []
    for index in range(0, EditRequest.objects.count()):
        fights_with_edit_request.append(EditRequest.objects.values_list('publication')[index][0])

    fights_with_delete_request = []
    for index in range(0, DeleteRequest.objects.count()):
        fights_with_delete_request.append(DeleteRequest.objects.values_list('publication')[index][0])

    if(publication.id in fights_with_edit_request or publication.id in fights_with_delete_request):
        return HttpResponse("You can't edit this publication while it is in awaiting state.")
    else:
        EditRequest.objects.create(publication=publication)
        return HttpResponseRedirect('/dashboard')

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

    fights_with_edit_request = []
    for index in range(0, EditRequest.objects.count()):
        fights_with_edit_request.append(EditRequest.objects.values_list('publication')[index][0])

    fights_with_delete_request = []
    for index in range(0, DeleteRequest.objects.count()):
        fights_with_delete_request.append(DeleteRequest.objects.values_list('publication')[index][0])
    
    if(publication.id in fights_with_edit_request or publication.id in fights_with_delete_request):
        return HttpResponse("You can't edit this publication while it is in awaiting state.")
    else:
        q = DeleteRequest.objects.create(publication = publication)
        q.save()
        return HttpResponseRedirect("/dashboard")

def new_publication_page(request):
    return render(request, 'FeathersFightApp/new_publication.html', {'form': QuillFieldForm()})

def new_publication_request(request):

    if(request.method != "POST"):
        return HttpResponse("Not a post method.")
    
    content = json.loads(request.POST["content"])
    
    title = request.POST["title"]
    text = content["html"]

    PublicationRequest.objects.create(title=title, text=text, author=request.user)

    return HttpResponseRedirect('/dashboard')