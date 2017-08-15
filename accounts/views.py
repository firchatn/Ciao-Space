from django.shortcuts import render
from .models import User


def add(request):
    return render(request, 'accounts/singup.html')
