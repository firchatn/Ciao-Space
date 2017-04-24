from django.shortcuts import render
from singup.models import users
from singup.forms import usersForms
from space.forms import post_forms
from space.forms import message_forms
from space.models import post
from space.models import messages
from django.utils import timezone
from space.models import cheekin
from decimal import *
locx = "" 
locy = "" 
vx = 0 
vy = 0 
def contrainer(request, urlloc):
	if request.method == "POST":
		form = usersForms(request.POST, request.FILES)
		if form.is_valid():
			newuser = users()	
			newuser.username = form.cleaned_data["username"] 
			newuser.name = form.cleaned_data["name"]
			newuser.lastname = form.cleaned_data["lastname"]
			newuser.email = form.cleaned_data["email"]
			newuser.password = form.cleaned_data["password"]
			newuser.selfi = form.cleaned_data["selfi"]
			start_date = timezone.now()
			newuser.save()
			compte = users.objects.all()[users.objects.count()-1]
			cheekin_v = cheekin()
			doc = urlloc.split("a")
			locx=doc[0].replace("p",".")
			locy=doc[1].replace("p",".")
			cheekin_v.username = users.objects.get(username = compte.username)
			cheekin_v.x = Decimal(locx)
			cheekin_v.y = Decimal(locy)
			cheekin_v.cheek_date = timezone.now()
			cheekin_v.save()
	compte = users.objects.all()[users.objects.count()-1]
	cheekin_compte = cheekin.objects.all()[cheekin.objects.count()-1]
	cheekin_view = cheekin.objects.all().order_by('-cheek_date')
	vx = float(cheekin_compte.x)
	vy = float(cheekin_compte.y)
	aux = [] # user in space of 2km of your current compte 
	for d in cheekin_view:
		m = float(d.x)
		n = float(d.y)
		if vx-0.2 < m < vx+0.2 and vy-0.2 < n < vy+0.2:
			f  =  users.objects.filter(username=d.username)
			aux.append(f)
	return render(request, 'space/index.html', {'vuser':aux , 'last':compte , 'cheekin' : cheekin_view , 'x' : urlloc})

def profil(request,urlloc, userspace):
	usee = users.objects.get(username=userspace)
	compte = users.objects.all()[users.objects.count()-1]
	postt = post.objects.all().order_by('-post_date')
	return render(request, 'space/profil.html', {'vuser':usee , 'last':compte , 't':urlloc , 'postt' : postt })


def new_post(request, urlloc, userspace):
	if request.method == "POST":
		form = post_forms(request.POST)
		if form.is_valid():
			new_post = post()
			new_post.title = form.cleaned_data["title"]
			new_post.aboutnow = form.cleaned_data["aboutnow"]
			new_post.post_date = timezone.now()
			new_post.username = users.objects.get(username= userspace)
			new_post.save()
	else:
		form = post_forms()
	compte = users.objects.all()[users.objects.count()-1]
	postt = post.objects.all().order_by('-post_date')
	return render(request, 'space/post.html', { 'form' : form , 'compte' : compte , 't' : urlloc , 'postt' : postt })


def message(request, urlloc, userspace):
	usee = users.objects.get(username=userspace)
	compte = users.objects.all()[users.objects.count()-1]
	cheekin_compte = cheekin.objects.all()[cheekin.objects.count()-1]
	cheekin_view = cheekin.objects.all().order_by('-cheek_date')
	vx = float(cheekin_compte.x)
	vy = float(cheekin_compte.y)
	aux = [] 
	for d in cheekin_view:
		m = float(d.x)
		n = float(d.y)
		if vx-0.2 < m < vx+0.2 and vy-0.2 < n < vy+0.2:
			f  =  users.objects.filter(username=d.username)
			aux.append(f)
	if request.method == "POST":
		form = message_forms(request.POST)
		if form.is_valid():
			newmsg = messages()	
			newmsg.body = form.cleaned_data["msg"]
			newmsg.toUser = users.objects.get(username= userspace) #to change for the correct user ! 
			newmsg.msg_date = timezone.now()
			newmsg.save()
	else:
		form = message_forms()
	return render(request, 'space/message.html', {'form' :form,  'vuser':usee , 'last':compte , 't':urlloc , 'vuser2':aux })

def logout(request):
	request.session[0] = 'logout'