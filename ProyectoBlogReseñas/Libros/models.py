from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Editorial(models.Model):
    nombre=models.CharField(max_length=40)
    email= models.EmailField()

    def __str__(self):
        return self.nombre
    
    class Meta:
        ordering = ["nombre"]

class Autor(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
    
    class Meta:
        ordering = ["apellido"]


class Libro(models.Model):
    titulo= models.CharField(max_length=100)
    isbn= models.CharField(max_length=30)
    fecha_publicacion = models.DateField()
    editorial = models.ForeignKey(Editorial,on_delete=models.CASCADE)
    autor = models.ForeignKey(Autor,on_delete=models.CASCADE)
    imagen=models.ImageField(null=True, blank=True, upload_to="imagenesLibros")
    
    def __str__(self):
        return f"{self.titulo}, de {self.autor}"
    
    class Meta:
        ordering = ["titulo"]


