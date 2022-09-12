from django import forms
from Libros.models import Editorial, Autor

class AutorFormulario(forms.Form):
    nombre=forms.CharField(max_length=30)
    apellido=forms.CharField(max_length=30)

class EditorialFormulario(forms.Form):
    nombre=forms.CharField(max_length=40)
    email=forms.EmailField()

class MyAutorChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.apellido  + " " + obj.nombre

class MyEditorialChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.nombre

class LibroFormulario(forms.Form):
    titulo= forms.CharField(max_length=100)
    autor = MyAutorChoiceField(queryset=Autor.objects.all())
    editorial = MyEditorialChoiceField(queryset=Editorial.objects.all())
    fecha_publicacion = forms.DateField()
    isbn= forms.CharField(max_length=30)
    imagen = forms.ImageField(required=False)

    #autor = models.ForeignKey(Autor,on_delete=models.CASCADE)