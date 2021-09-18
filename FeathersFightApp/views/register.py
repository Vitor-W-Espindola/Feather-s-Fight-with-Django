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


from FeathersFightApp.models import PublicationRequest, Fight


def removeTags(html):
    soup = BeautifulSoup(html, "html.parser")
    for data in soup(['style', 'script']):
        data.decompose()
  
    # return data by retrieving the tag content
    return ' '.join(soup.stripped_strings)   


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
