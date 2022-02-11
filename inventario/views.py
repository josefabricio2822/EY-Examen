from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from .models import Articulo
from django.urls import reverse

# Create your views here.
class ArticuloListView(ListView):
    model = Articulo

class ArticuloCreateView(CreateView):
    model = Articulo
    fields = ['codigoArticulo', 'nombreArticulo','descripcionArticulo','cantidadArticulo']
    success_url = '/'

class ArticuloUpdateView(UpdateView):
    model = Articulo
    fields = ['codigoArticulo', 'nombreArticulo','descripcionArticulo','cantidadArticulo']
    success_url = '/'
    def get_absolute_url(self):
        return reverse('articulo-list')

class ArticuloDeleteView(DeleteView):
    model = Articulo
    success_url = '/'