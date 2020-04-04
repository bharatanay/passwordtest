from django.shortcuts import render
import random
from django.http import HttpResponse


def index(request):
    return render(request, 'generate/index.html', {'name': 'bharat'})

def about(request):
    return render(request, 'generate/about.html')


def password(request):
    passd = ''
    character = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length', 10))
    if request.GET.get('uppercase'):
        character.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('number'):
        character.extend(list('1234567890'))
    if request.GET.get('special'):
        character.extend(list('!@#$%^&*()_~'))
    for x in range(length):
        passd += random.choice(character)

    return render(request, "generate/password.html", {'password': passd})

# Create your views here.
