from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'generator\home.html')

def password(request):
    thepassword='testing'

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    # в реквесте с шаблона html передается инфа от пользователя
    length=int(request.GET.get('length', 12)) # 12 - значение по умолчанию

    thepassword=''

    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator\password.html', {'password':thepassword})

def site_about(request):
    
    if request.GET.get('uppercase'):
        text='THIS IS TESTING APP WAS MADE BY DMITRY P. FOR AIM OF LEARNING DJANGO'
    else:
        text='This is testing app was made by Dmitry P. for aim of learning django'

    return render(request, 'generator\site_about.html', {'param_uppercase':text})
