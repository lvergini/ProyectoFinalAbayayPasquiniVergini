from django.shortcuts import render
from .forms import *
from django.contrib.auth.decorators import login_required
from .models import *
from Libros.models import Libro


# Create your views here.
def inicio(request):
      return render(request, "Blog/inicio.html")

def about(request):
      return render(request, "Blog/about.html")

@login_required
def crearPost(request):
    if request.method=="POST":
        form=CrearPost(request.POST, request.FILES)
        if form.is_valid():
            autor=User.objects.get(username=request.user) #ESTO ES IMPORTANTE!!!!!!!!!!!!!!!!!11
            info=form.cleaned_data
            titulo= info['titulo']
            subtitulo= info['subtitulo']
            # libro= Libro.objects.get(id = info["libro"].id)
            # imagen= info['imagen']
            cuerpo=info['cuerpo']
            post=Post(titulo=titulo, subtitulo=subtitulo, cuerpo=cuerpo, autor=autor)
            post.save()
            return render(request, "Blog/inicio.html", {"mensaje": f"Se creó el post {titulo}"})
        else:
            return render(request, "Blog/inicio.html", {"mensaje": "Error. Se ingresaron mal los datos"})
    
    else:
        form=CrearPost()
        return render(request, "blog/crearPost.html", {"form": form})

def verPost(request, pk):
      post=Post.objects.filter(id=pk)
      if len(post)!=0:
            post = post[0]
            return render(request, "Blog/verPost.html", {"post":post})
      else: 
            return render (request, "Blog/inicio.html", {"mensaje": "No hay páginas aún"}) 

                  
#Para mostrar todas las publicaciones
def pages(request):
      lista_post=Post.objects.all()
      return render(request, "Blog/pages.html", {"lista_post": lista_post })

#Elimiar publicación (Falta restringir la función sólo a la persona que lo creó)
def eliminarPost(request, id):
      posteo=Post.objects.get(id=id)
      posteo.delete()
      lista_post=Post.objects.all()
      return render(request, "Blog/pages.html", {"lista_post": lista_post })
      
#Para modificar una publicación
""" def editarPost(request, id):
      posteo=Post.objects.get(id=id)
      if request.method=="POST":
           form=CrearPost(request.POST)
           if form.is_valid():
                  info=form.cleaned_data
                  posteo. =info[""] """


