from django.shortcuts import render

from . import mongo

def user(request):
    return render(request, 'user.html')