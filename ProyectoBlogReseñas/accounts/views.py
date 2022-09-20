from django.shortcuts import render
from accounts.forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from Blog.models import Post

@login_required
def messages(request):
    if request.method=="POST":
        form=EnvioMensaje(request.POST)
        if form.is_valid(): 
            _emisor = User.username
            mensaje=Mensaje(emisor=request.user,
                            receptor=form.cleaned_data["receptor"], 
                            texto=form.cleaned_data["mensaje"])
            mensaje.save()
            return render(request, "accounts/messages.html", {"mensaje": f"valido"})
    else:
        form=EnvioMensaje()
    return render(request, "accounts/messages.html", {"form":form})

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

def profile(request, pk):
    usuario=User.objects.filter(pk=pk)
    if len(usuario)!=0:
        usuario=usuario[0]
        posts=Post.objects.filter(autor=usuario)
        return render(request, "accounts/profile.html", {"usuario":usuario, "posts":posts})
    else:
        return render(request, "Blog/inicio.html", {"mensaje":"No hay usuarios con esos datos"})

@login_required
def editarPerfil(request):
    if request.method =="POST":
        form_usuario = UserEditForm(request.POST, instance=request.user)
        form_perfil = ProfileEditForm(request.POST, request.FILES, instance=request.user.perfil)
        if form_usuario and form_perfil:
            form_usuario.save()
            form_perfil.save()
            user=request.user
            pk=user.pk
            return render(request, "accounts/profile.html", {"pk":pk})
    else:
        form_usuario = UserEditForm(instance=request.user)
        form_perfil = ProfileEditForm(instance=request.user.perfil)

    return render(request, 'accounts/editarPerfil.html',{'form_usuario': form_usuario, 'form_perfil': form_perfil})
