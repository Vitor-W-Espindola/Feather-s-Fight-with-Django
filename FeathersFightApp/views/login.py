from django.http.response import HttpResponseRedirect
from django.http import HttpResponse
from django.template import loader
from django.contrib import auth

# This method is used to retrieve the login page
def login_page(request):
    template = loader.get_template('FeathersFightApp/login.html')
    return HttpResponse(template.render({}, request))

# This method is used to process a log in
# when the url localhost:8000/login/success is required
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

# This method is used to process a log out
# when the url localhost:8000/logout
def logout_process(request):
    auth.logout(request)
    return HttpResponseRedirect('/')
