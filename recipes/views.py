from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'recipes/home.html', context={'name': 'luis gustavinho'})


def contato(request):
    return render(request, 'recipes/contato.html', context={'name': 'luis gustavinho'})


def sobre(request):
    return HttpResponse('SOBRE')
