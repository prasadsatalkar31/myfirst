from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import signup,questions
from django.http import HttpRequest,HttpResponse
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
import csv
from django.conf import settings
from django.contrib.auth.models import User
import random
def db():
    s=settings.BASE_DIR+'/app/static/questions.csv'
    with open(s) as csvfile:
        reader = csv.DictReader(csvfile)
        i=0
        for row in reader:
            que= row['Question']
            op1= row['Option 1']
            op2= row['Option 2']
            op3= row['Option 3']
            op4= row['Option 4']
            ans=row['Answer']
            x=questions(question=que,op1=op1,op2=op2,op3=op3,op4=op4,ans=ans)
            x.save()
            user = User.objects.create_user('sanika','sanikashah1110@gmail.com', 'akinas')
            user.save()

def index(request):
	con={}
	return render(request,'app/home.html',con)

#@login_required
def check(request):
    if request.POST.get("login-button"):
            name=request.POST.get("username")
            password=request.POST.get("password")
            print name
            print password
            s=authenticate(username=name,password=password)
            print s
            if s:
                login(request,s)
                r=random.randint(1,23)
                q=questions.objects.get(id=r)
                con={
                    "q":q
                }
                print q
                return render(request,'app/samp.html',con)
            else:
                return HttpResponse("j1 zala ka?")
    else:
        return HttpResponse("Request not received")

def ques(request):
                r=random.randint(1,23)
                q=questions.objects.get(id=r)
                con={
                    "q":q
                }
                print q
                return render(request,'app/samp.html',con)
