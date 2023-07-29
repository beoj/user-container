'''
Xử lí các request
'''

from django.shortcuts import render

from . import mongo

def user(request):
    '''
    Xử lý request cho /user
    '''
    context = {

    }
    return render(request, 'user.html', context=context)