from django.http.response import HttpResponseRedirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User, Group
from django.contrib import auth

# This method is used to retrieve the author registration page
def register_author_page(request):
    template = loader.get_template('FeathersFightApp/register_author.html')
    return HttpResponse(template.render({}, request))

# This method is used to process an author registration
# when the url localhost:8000/register_author/success is required
def register_author_process(request):
    
    if(request.method != "POST"):
        return HttpResponse("Not a post method.")
    
    username = request.POST["username"]
    email = request.POST["email"]
    password = request.POST["password"]
    confirm_password = request.POST["confirm_password"]

    # If passwords do not match
    if(password != confirm_password):
        return HttpResponse('Passwords do not match.')
    
    # If a field is empty
    if(username != "" and email != "" and password != "" and confirm_password != ""):
        
        username_exist = User.objects.filter(username=username)
        email_exist = User.objects.filter(email=email)
    
        # If user and email are not registered
        if(len(username_exist) == 0 and len(email_exist) == 0):
            user = User.objects.create_user(username=username, email=email, password=password)
            authors= Group.objects.get(name="Authors")
            authors.user_set.add(user)
            user.save()
            auth.login(request, user)
            return HttpResponseRedirect('/')
        else:
            return HttpResponse('User already registered.')
    else:
        return HttpResponse("Fill all form fields.")

