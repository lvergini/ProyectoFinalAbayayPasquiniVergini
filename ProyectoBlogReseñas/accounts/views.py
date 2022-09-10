from django.shortcuts import render
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def register(request):
    if request.method=="POST":
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            form.save()
            return render(request, "AppLibros/inicio.html", {"mensaje": f"Usuario {username} creado"})
    else:
        form=UserRegisterForm()
    return render(request, "accounts/register.html", {"form":form})