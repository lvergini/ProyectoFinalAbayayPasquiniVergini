from django import forms
from Blog.models import *
from ckeditor.widgets import CKEditorWidget
from Libros.models import Libro

class MyLibroChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.titulo

class CrearPost(forms.Form):
    titulo= forms.CharField(max_length=250)
    subtitulo=forms.CharField(max_length=250)
    libro=MyLibroChoiceField(queryset=Libro.objects.all())
    imagen= forms.ImageField(required=False, label="Imagen")
    cuerpo=forms.CharField(widget=CKEditorWidget, max_length=500)



