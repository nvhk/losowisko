from django.shortcuts import render
from django.http import HttpResponse
from .models import Ludzie
from django.contrib import messages
import random

def index(request):
    entries = Ludzie.objects.all()

    return render(request, 'losowisko1/index.html', {'entries': entries})

def wynik(request):

    osoby = request.GET.getlist('osoby')

    if not osoby:
        osoby.append('Ty xD')

    twujstary = ['Dafko', 'Macias', 'Kuba', 'Pszemek', 'Rafas']
    if osoby == twujstary:
         osoby.clear()
         osoby = ['Twuj stary pijany']



    return render(request, 'losowisko1/wynik.html', {'wygrany':(random.choice(osoby))})
