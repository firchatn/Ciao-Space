from django.shortcuts import render
from singup.models import users
from singup.forms import usersForms


def add(request):
    return render(request, 'singup/singup.html')
