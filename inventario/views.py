from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Articulo
# Create your views here.

def home(request):
  return HttpResponse("Hola Mundo. Te encuentras en la página de inicio del EY Express")

class ArticuloListView(ListView):
    model = Articulo

class ArticuloDetailView(DetailView):
    model = Articulo