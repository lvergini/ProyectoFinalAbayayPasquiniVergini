from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class UserRegisterForm(UserCreationForm):
    first_name=forms.CharField(label="Nombre", max_length=50, required=True)
    last_name = forms.CharField(label="Apellido", max_length=50, required=True)
    email=forms.EmailField(required=True)
    descripcion = forms.CharField(widget=forms.Textarea, max_length=500, required=False)
    pagina_web=forms.URLField()
    #imagen = forms.ImageField(required=False, upload_to="imagenesPerfil")
    password1: forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2: forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}