from django.shortcuts import render
from singup.models import User


def add(request):
    return render(request, 'singup/singup.html')
