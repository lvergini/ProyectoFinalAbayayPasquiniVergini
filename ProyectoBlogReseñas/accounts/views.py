from django.shortcuts import render, redirect
from accounts.forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from Blog.models import Post
from Blog.views import obtenerCategorias
from django.urls import reverse


@login_required
def mensajeAUsuario(request, usu):
    if request.method=="POST":
        form=MensajeUsuario(request.POST)
        if form.is_valid(): 
            emisor = User.objects.get(username=request.user)
            receptor=User.objects.filter(username=usu)
            receptor=receptor[0]
            mensaje=Mensaje(emisor=emisor,
                            receptor=receptor, 
                            texto=form.cleaned_data["mensaje"])
            mensaje.save()
            return render(request, "accounts/messagesUsu.html", {"usu": usu, "receptor":receptor, "mensaje": f"Mensaje enviado correctamente a {receptor}"})
    else:
        form=MensajeUsuario()
    return render(request, "accounts/messagesUsu.html", {"usu":usu, "form":form})
#SI ELIMINAMOS EL MENSAJE GENERAL, CAAMBIEMOS LA URL DE ESTE A MESSAGES

@login_required
def conversacion(request, usu):
    perfiles=Perfil.objects.exclude(user=request.user)
    contacto=User.objects.filter(username=usu)
    contacto=contacto[0]
    mensajesConUsuario=[]
    usuario=request.user
    mensajesMandados=Mensaje.objects.filter(emisor=usuario)
    for mensaje in mensajesMandados:
        receptor=mensaje.receptor
        if receptor==contacto:
            mensajesConUsuario.append(mensaje)
    mensajesRecibidos=Mensaje.objects.filter(receptor=usuario)
    for mensaje in mensajesRecibidos:
        emisor=mensaje.emisor
        if emisor==contacto:
            mensajesConUsuario.append(mensaje)
    mensajesConUsuario= sorted(mensajesConUsuario, key=lambda mensaje: mensaje.fecha)

    return render(request, "accounts/conversacion.html", {"usu":usu, "usuario":usuario, "contacto": contacto, "perfiles": perfiles, "mensajesConUsuario":mensajesConUsuario, "categorias": obtenerCategorias(request)} )

  
def signup(request):
    if request.method=="POST":
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            form.save()
            return render(request, "Blog/inicio.html", {"mensaje": f"Usuario {username} creado"})
    else:
        form=UserRegisterForm()
    return render(request, "accounts/signup.html", {"form":form, "categorias": obtenerCategorias(request)})

def home(request):
     posts=Post.objects.all()       
     return render(request, 'Blog/inicio.html',{ 'posts': posts })

def login_request(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usu=form.cleaned_data.get('username')
            clave=form.cleaned_data.get('password')

            usuario=authenticate(username=usu, password=clave)

            if usuario is not None:
                login(request, usuario)
                posts=Post.objects.all()
             
                return render(request, 'Blog/inicio.html', {'mensaje':f"Bienvenido {usuario}", 'posts': posts })
            else:
                return render(request, 'accounts/login.html',{"form":form,'mensaje': "Usuario o contraseña incorrectos"})
            
        else:
            return render(request, 'accounts/login.html',{"form":form,'mensaje': "Usuario o contraseña incorrectos"})
    else:
        form=AuthenticationForm()
        return render(request, 'accounts/login.html',{"form":form, "categorias": obtenerCategorias(request)})

def profile(request, pk):
    usuario=User.objects.filter(pk=pk)
    if len(usuario)!=0:
        usuario=usuario[0]
        posts=Post.objects.filter(autor=usuario)
        return render(request, "accounts/profile.html", {"usuario":usuario, "posts":posts, "categorias": obtenerCategorias(request)})
    else:
        return render(request, "Blog/inicio.html", {"mensaje":"No hay usuarios con esos datos"})

@login_required
def editarPerfil(request):
    if request.method =="POST":
        form_usuario = UserEditForm(request.POST, instance=request.user)
        form_perfil = ProfileEditForm(request.POST, request.FILES, instance=request.user.perfil)
        usuario= request.user
        posts=Post.objects.filter(autor=usuario)
        if form_usuario and form_perfil:
            form_usuario.save()
            form_perfil.save()
            user=request.user
            pk=user.pk
            return render(request, "accounts/profile.html", {"pk":pk, "usuario": usuario, "posts":posts})
        else:
            return render(request, "accounts/editarPerfil.html", {"pk":pk, "mensaje": "Error. Se ingresaron mal los datos", 'form_usuario': form_usuario, 'form_perfil': form_perfil, "usuario": usuario, "posts":posts})
    
    else:
        form_usuario = UserEditForm(instance=request.user)
        form_perfil = ProfileEditForm(instance=request.user.perfil)

    return render(request, 'accounts/editarPerfil.html',{'form_usuario': form_usuario, 'form_perfil': form_perfil})

def listaPerfiles(request):
    perfiles=Perfil.objects.all()
    return perfiles