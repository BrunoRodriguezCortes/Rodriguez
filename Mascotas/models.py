from django.db import models



class Mascotas(models.Model):
    articulo = models.CharField(primary_key=True, max_length=8, verbose_name="articulo")
    marca = models.CharField(max_length=50, blank=True, verbose_name="Marca")
    imagen = models.ImageField(upload_to="imagenes",null=True,blank=True,verbose_name="Imagen")


    def __str__(self):
        return self.articulo

# Create your models here.
