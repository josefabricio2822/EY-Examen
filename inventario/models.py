from django.db import models

# Create your models here.

class Articulo(models.Model):
    codigoArticulo=models.CharField(max_length=7)
    nombreArticulo=models.CharField(max_length=50)
    descripcionArticulo=models.CharField(max_length=200)
    cantidadArticulo=models.IntegerField()

def sku(self):
      codigo_articulo = self.codigoArticulo()
      return f'{codigo_articulo}'