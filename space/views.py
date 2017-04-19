from django.shortcuts import render
from singup.models import users
from singup.forms import usersForms
from space.forms import post_forms
from space.models import post
from django.utils import timezone
from space.models import cheekin
from decimal import *
locx = ""
locy = "" 
vx = 0 
vy = 0 
def contrainer(request, x):
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
			newuser.save()
			usee = users.objects.all()
			compte = users.objects.all()[users.objects.count()-1]
			cheekin_v = cheekin()
			doc = x.split("a")
			locx=doc[0].replace("p",".")
			locy=doc[1].replace("p",".")
			cheekin_v.username = users.objects.get(username = compte.username)
			cheekin_v.x = Decimal(locx)
			cheekin_v.y = Decimal(locy)
			cheekin_v.cheek_date = timezone.now()
			cheekin_v.save()
	usee = users.objects.all()
	compte = users.objects.all()[users.objects.count()-1]
	cheekin_compte = cheekin.objects.all()[cheekin.objects.count()-1]
	cheekin_view = cheekin.objects.all().order_by('-cheek_date')
	vx = float(cheekin_compte.x)
	vy = float(cheekin_compte.y)
	aux = []
	print "list user in "
	for d in cheekin_view:
		m = float(d.x)
		n = float(d.y)
		if vx-0.2 < m < vx+0.2 and vy-0.2 < n < vy+0.2:
			print d.username
			f  =  users.objects.filter(username=d.username)
			aux.append(f)
			for j in f:
				print f[0].name
			#fixe this by new template for echtach profil 
			#load bloc in index 

	return render(request, 'space/index.html', {'vuser':usee , 'vuser2':aux , 'last':compte , 'cheekin' : cheekin_view , 'x' : x})

def profil(request,t, userspace):
	usee = users.objects.get(username=userspace)
	compte = users.objects.all()[users.objects.count()-1]
	postt = post.objects.all()
	return render(request, 'space/profil.html', {'vuser':usee , 'last':compte , 't':t , 'postt' : postt })


def new_post(request, t, userspace):
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
	t=t
	postt = post.objects.all().order_by('-post_date')
	return render(request, 'space/post.html', { 'form' : form , 'compte' : compte , 't' : t , 'postt' : postt })


def message():
	return True
