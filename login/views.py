from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request) :
    return render(request,'login/backend-login.html',context_instance=RequestContext(request))

def user_login(request) :
    if request.method == 'POST' :
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == 'abcvivek' :
            user = authenticate(username=username,password=password)
            login(request,user)
            return HttpResponseRedirect(reverse('dashboard:theatre-manager-view'))
        else : 
            print('Login Failed')
            return HttpResponse("Login Failed")

    else :
        return render(request,'login/backend-login.html') 

@login_required
def user_logout(request) :
    logout(request)
    return HttpResponseRedirect(reverse('login:user_login'))