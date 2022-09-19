from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget



class UserRegisterForm(UserCreationForm):
    # first_name=forms.CharField(label="Nombre", max_length=50, required=True)
    # last_name = forms.CharField(label="Apellido", max_length=50, required=True)
    email=forms.EmailField(required=True)
    username=forms.CharField(required=True)
    #descripcion = forms.CharField(widget=forms.Textarea, max_length=500, required=False)

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
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = [ 'email', 'first_name', 'last_name',  'password1', 'password2']
        help_texts = {k:"" for k in fields}


class ProfileEditForm(forms.ModelForm):
    imagen = forms.ImageField(required=False)
    descripcion = forms.CharField(widget=CKEditorWidget, required=False, max_length=500)
    pagina_web=forms.URLField(required=False)

    class Meta:
        model = Perfil
        fields = ['imagen', 'descripcion', 'pagina_web']
        help_texts = {k:"" for k in fields}
