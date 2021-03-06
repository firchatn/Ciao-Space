from django.shortcuts import render, redirect
from accounts.forms import UserForm


def index(request):
    return render(request, 'welcome/home.html')


def start(request, x):
    request.session[0] = "none"
    print(request.session[0])
    if request.method == "POST":
        if request.session[0] == "login":
            print(request.session[0])
            return render(request, 'space/index.html')
        else:
            request.session[0] = "login"
            form_class = UserForm()
            return render(request, 'accounts/singup.html', {
                'form': form_class, 'x': x
            })
    else:
        return render(request, 'welcome/error404.html')
