from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from ckeditor.widgets import CKEditorWidget

class MyReceptorChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.username

class EnvioMensaje(forms.Form):
      emisor = User
      receptor = MyReceptorChoiceField(queryset=User.objects.all())
      mensaje = forms.CharField(widget=forms.Textarea, max_length=500)
      
class MensajeUsuario(forms.Form):
    mensaje=forms.CharField(widget=forms.Textarea, max_length=500)


class UserRegisterForm(UserCreationForm):
    email=forms.EmailField(required=True)
    username=forms.CharField(required=True)

    password1: forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2: forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

        for fieldname in ['email', 'username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    class Meta:
        model=User
        fields=['email', 'username', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class UserEditForm(forms.ModelForm):
    email = forms.EmailField(label="Modificar E-Mail")
    first_name = forms.CharField(label='Modificar Nombre')
    last_name = forms.CharField(label='Modificar Apellido')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput, required=False)
    
    class Meta:
        model = User
        fields = [ 'email', 'first_name', 'last_name',  'password1', 'password2']
        help_texts = {k:"" for k in fields}


class ProfileEditForm(forms.ModelForm):
    imagen = forms.ImageField(required=False)
    descripcion = forms.CharField(widget=CKEditorWidget, max_length=6000, required=False)
    pagina_web=forms.URLField(required=False)
    profesion=forms.CharField(max_length=60, required=False)
    pais=forms.CharField(max_length=60, required=False)
    instagram=forms.URLField(required=False)
    linkedin=forms.URLField(required=False)

    class Meta:
        model = Perfil
        fields = ['imagen', 'descripcion', 'pagina_web', 'pais', 'profesion', 'instagram', 'linkedin']
        help_texts = {k:"" for k in fields}
