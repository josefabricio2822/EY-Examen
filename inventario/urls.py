from django.urls import path

from . import views

urlpatterns = [
    path('', views.ArticuloListView.as_view(), name='articulo-list'),
    path('articulo/new/', views.ArticuloCreateView.as_view(), name='articulo-create'),
    path('articulo/<int:pk>/update/', views.ArticuloUpdateView.as_view(), name='articulo-update'),
    path('articulo/<int:pk>/delete/', views.ArticuloDeleteView.as_view(), name='articulo-delete'),
]
