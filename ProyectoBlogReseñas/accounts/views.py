from django.shortcuts import render
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def signup(request):
    if request.method=="POST":
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            form.save()
            return render(request, "Blog/inicio.html", {"mensaje": f"Usuario {username} creado"})
    else:
        form=UserRegisterForm()
    return render(request, "accounts/signup.html", {"form":form})

def login_request(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usu=form.cleaned_data.get('username')
            clave=form.cleaned_data.get('password')

            usuario=authenticate(username=usu, password=clave)

            if usuario is not None:
                login(request, usuario)
                return render(request, 'Blog/inicio.html', {'mensaje':f"Bienvenido {usuario}"})
            else:
                return render(request, 'accounts/login.html',{"form":form,'mensaje': "Usuario o contraseña incorrectos"})
            
        else:
            return render(request, 'accounts/login.html',{"form":form,'mensaje': "Usuario o contraseña incorrectos"})
    else:
        form=AuthenticationForm()
        return render(request, 'accounts/login.html',{"form":form})
