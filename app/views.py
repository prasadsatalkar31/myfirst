from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import signup,questions
from django.http import HttpRequest,HttpResponse
from django.contrib.auth import authenticate, login
from django.http import HttpResponse


def index(request):
	con={}
	return render(request,'signup/home.html',con)

#@login_required
def check(request):
    if request.POST.get("login-button"):

            name=request.POST.get("username")
            password=request.POST.get("password")
            print name
            print password
            s=authenticate(username=name,password=password)
            if s:
                login(request,s)
                q=questions.objects.order_by('?')
                con={
                    "q":q
                }
                print q
                return render(request,'signup/samp.html',con)
            else:
                return HttpResponse("j1 zala ka?")
    else:
        return HttpResponse("Request not received")


def ques(request):
    pass


