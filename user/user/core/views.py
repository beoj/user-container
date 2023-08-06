'''
Xử lí các request
'''

from django.shortcuts import render

from . import models

def user(request):
    '''
    Xử lý request cho /user
    '''

    userArr = list(models.User.manyFromDatabase({}))
    userArr.sort(key=lambda x: x.point)

    context = {
        "userArr" : userArr,
    }
    return render(request, 'user.html', context=context)