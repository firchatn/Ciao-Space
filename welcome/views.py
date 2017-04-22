from django.shortcuts import render
from singup.forms import usersForms

#def isuser(request):
#	return request.session['status'] == "login"

def startapp(request):
	return render(request, 'welcome/home.html')

def start(request, x):
	if request.method == "POST":
		request.session[0] = 'login'
		if request.session[0] == "login":
			return render(request, 'space/index.html')
		else:
			form_class = usersForms()
			return render(request, 'singup/singup.html', {
				'form': form_class, 'x' : x 
    })
	else:
		return render(request, 'welcome/home.html')
		#to change return httpsreponse page error 404 !
