from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from Libros.models import Libro
from ckeditor.fields import RichTextField


class Categoria(models.Model):
    nombre=models.CharField(max_length=50, null=True)
    
    class Meta:
        ordering = ["nombre"]
    
    def __str__(self):
        return self.nombre

class Post(models.Model):
    titulo = models.CharField(max_length=250)
    subtitulo=models.CharField(max_length=250)
    autor=models.ForeignKey(User, on_delete=models.CASCADE)
    categoria=models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    libro=models.ForeignKey(Libro, on_delete=models.CASCADE, null=True)
    imagen=models.ImageField(null=True, blank=True, upload_to="imagenesBlog")
    cuerpo=RichTextField()
    fecha_publicacion=models.DateTimeField(auto_now_add=True)
    likes=models.ManyToManyField(User, related_name='likes')

    class Meta:
        ordering = ["-fecha_publicacion"]

    def cantidad_likes(self):
        return self.likes.count()


    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, related_name='comentarios') # la opción related_namme nos permite acceder acceso a los comentarios desde el modelo Post.
    autor = models.ForeignKey(User, on_delete=models.SET_NULL,  null=True, blank=True)  #OTRA OPCIÓN: settings.AUTH_USER_MODEL,# CHEQUEAR SI ES NECESARIO ASÍ, O COMO ESTABA ANTES. 
    comentario = models.TextField(max_length=1000, null=True)
    fecha_comentario = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ["fecha_comentario"]

    def __str__(self):
        return f'{self.autor}, {self.post.titulo}, {self.fecha_comentario}'