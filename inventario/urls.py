from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('articulos', views.ArticuloListView.as_view(), name='Articulo-list'),
]
