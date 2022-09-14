from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField
from Libros.models import Libro

class Categoria(models.Model):
    pass

class Post(models.Model):
    titulo = models.CharField(max_length=250)
    subtitulo=models.CharField(max_length=250)
    autor=models.ForeignKey(User, on_delete=models.CASCADE)
    # libro=models.ForeignKey(Libro, on_delete=models.CASCADE, null=True)
    imagen=models.ImageField(null=True, blank=True, upload_to="imagenesBlog")
    cuerpo=RichTextField()
    fecha_publicacion=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.titulo




class Comentario(models.Model):
    pass
