from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.conf import settings
from .models import Signup, Questions
import csv,random

# Create your views here.
name = ""
mylist=[]
mylist2=""

def db():
    s=settings.BASE_DIR+'/static/questions.csv'
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
            x=Questions(question=que,op1=op1,op2=op2,op3=op3,op4=op4,ans=ans)
            x.save()

def index(request):
    return render(request, "round1/index.html",{})

def signup(request):
    if request.POST.get("login-button"):
		global name
		global mylist
		name = request.POST.get("username")
		password = request.POST.get("password")

		print name,password
		s= Signup.objects.filter(userid=name,password=password)
		if s:
			uname=name
			so=Signup.objects.get(userid=uname)
			mylist=map(str,so.array.split(';'))
			if mylist[0]=='':
				return HttpResponseRedirect('/')
			print mylist
			mlist=map(int,mylist)
			print mlist
			value = random.choice(mlist)
			mlist.remove(value)
			print value
			print mlist
			mylist2=";".join(str(x) for x in mlist)
			so.array=mylist2
			so.save()
			print so.array
			q=Questions.objects.get(id=value)
			con={
			    "q":q,
			    "s":so
			}
			print so.userid,so.timestamp
			return render(request,'round1/questions.html',con)
		else:
			return HttpResponse("Invalid")
    else:
        return render(request, "round1/signup.html",{})

def questions(request):
    con={}
    so=Signup.objects.get(userid=name)
    con['s']=so
    if request.POST.get('next'):
        global mylist
        global name
        mylist=map(str,so.array.split(';'))
        if mylist[0]=='':
            return HttpResponseRedirect('/')
        #print mylist
        mlist=map(int,mylist)
        #print mlist
        value = random.choice(mlist)
        mlist.remove(value)
        #print value
        #print mlist
        #print mlist
        mylist2=";".join(str(x) for x in mlist)
        so.array=mylist2
        so.save()
        #print so.array
        q=Questions.objects.get(id=value)
        con['q']=q
        #print q
        return render(request,"round1/questions.html",con)
    else:
        return render(request,"round1/questions.html",con)

def update_state(request):
	print "Ajax"
	if request.method == "POST":
		print "aala"
		if request.is_ajax():
			uid = request.POST.get("uid")

			print "uid"
			s=Signup.objects.get(userid=uid)
			s.timestamp = s.timestamp-10
			s.save()

			return questions(request)
	else:
		return questions(request)
