from django.shortcuts import render
from django.http import HttpResponse

from apps.app1.models import Contatos1

dados = Contatos1.objects.all()
#def index(requisicao):
    #return HttpResponse("<h1> ****Meu primeiro APP em Django****</h1>")

def index(requisicao):
    return render(requisicao,'index.html') #index.html

def arearestrita(requisicao):
    return render(requisicao,'area_restrita1.html')

def home(requisicao):
    return render(requisicao,'home.html',{"Contatos1":dados})


# Create your views here.
