from django.shortcuts import render, get_object_or_404
from .forms import *
from django.contrib.auth.decorators import login_required
from .models import *
from Libros.models import Libro
from django.http import HttpResponseRedirect
from django.urls import reverse

#--------------Inicio y about------------------------------------------------------------

def inicio(request):

      return render(request, "Blog/inicio.html", {"categorias": obtenerCategorias(request)})
    
def about(request):
      return render(request, "Blog/about.html", {"categorias": obtenerCategorias(request)})

#--------------Posts------------------------------------------------------------

@login_required
def crearPost(request):
    if request.method=="POST":
        form=CrearPost(request.POST, request.FILES)
        if form.is_valid():
            autor=User.objects.get(username=request.user) 
            info=form.cleaned_data
            titulo= info['titulo']
            subtitulo= info['subtitulo']
            categoria=Categoria.objects.get(pk = info["categoria"].id)
            libro= Libro.objects.get(pk = info["libro"].id)
            imagen= info['imagen']
            cuerpo=info['cuerpo']
            post=Post(titulo=titulo, subtitulo=subtitulo, categoria=categoria, libro=libro, imagen=imagen, cuerpo=cuerpo, autor=autor)
            post.save()
            return render(request, "Blog/inicio.html", {"mensaje": f"Se creó el post {titulo}"})
        else:
            return render(request, "Blog/inicio.html", {"mensaje": "Error. Se ingresaron mal los datos"})
    
    else:
        form=CrearPost()
        return render(request, "Blog/crearPost.html", {"form": form})

@login_required
def likeView(request, pk):
      post = get_object_or_404(Post, id=request.POST.get('post_id'))
      liked=False

      if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)

      else:
            post.likes.add(request.user)

      return HttpResponseRedirect(reverse("PostVista", args=[str(pk)]))

def postVista(request, pk):
      post=Post.objects.filter(id=pk)
      if len(post)!=0:
            post = post[0]
            comentarios=Comentario.objects.filter(post=post.id)
            cantidad_likes=post.cantidad_likes()
            liked=post.likes.filter(id=request.user.id)
            if len(liked)!=0:
                  liked=True
            
            else:
                  liked=False

            return render(request, "Blog/post.html", {"post":post, "comentarios":comentarios, "cantidad_likes":cantidad_likes, "liked":liked, "categorias": obtenerCategorias(request)})
      else: 
            return render (request, "Blog/inicio.html", {"mensaje": "No se ha encontrado ningún post. Pruebe buscar de nuevo."}) 
                
#Para mostrar todas las publicaciones
def listaPosts(request):
      posts=Post.objects.all()
      return render(request, "Blog/pages.html", {"posts": posts, "categorias": obtenerCategorias(request)})

#YA RESTRINGÍ, falta agregar pag de confirm de eliminación - Elimiar publicación (Falta restringir la función sólo a la persona que lo creó)
@login_required
def eliminarPost(request, id):
      posteo=Post.objects.get(id=id)
      posteo.delete()
      posts=Post.objects.all()
      return render(request, "Blog/pages.html", {"posts": posts })
      
#Para modificar una publicación
""" def editarPost(request, id):
      posteo=Post.objects.get(id=id)
      if request.method=="POST":
           form=CrearPost(request.POST)
           if form.is_valid():
                  info=form.cleaned_data
                  posteo. =info[""] """

def busquedaPost(request):
    return render(request, "Blog/busquedaPost.html")

def buscarPost(request): #para completar
      pass

#--------------Categorías------------------------------------------------------------

def crearCategoria(request):
    if request.method=="POST":
        form=CrearCategoria(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            categoria=Categoria(nombre=nombre)
            categoriaEnBase=Categoria.objects.filter(nombre=nombre)
            if len(categoriaEnBase)!=0:
                return render(request, "Blog/crearCategoria.html", {"mensaje": f"Ya existe la categoría {nombre}", "form":form})
            else: 
                categoria.save()
            return render(request, "Blog/inicio.html", {"mensaje": f"Se creó la categoría {nombre}"})
        else:
            return render(request, "Blog/crearCategoria.html", {"mensaje": "Error. Se ingresaron mal los datos"})
    
    else:
        form=CrearCategoria()
        return render(request, "Blog/crearCategoria.html", {"form": form, "categorias": obtenerCategorias(request)})

def categoriaPosts(request, cat):
      categoria=Categoria.objects.filter(nombre=cat.replace('-', ' '))
      if len(categoria)!=0:
            categoria_posts=Post.objects.filter(categoria__nombre=cat.replace('-', ' '))
            return render(request, "Blog/categoria.html", {"cat":cat.title().replace('-', ' '), "categoria_posts":categoria_posts} )
      else:
            return render(request, "Blog/categoria.html", {"cat":cat.title().replace('-', ' '), "mensaje": f"Todavía no fue creada la categoría {cat}"} )

def obtenerCategorias(request):
      categorias=Categoria.objects.all()
      return categorias

#--------------Comentarios------------------------------------------------------------

@login_required
def crearComentario(request, pk):
      post= Post.objects.get(pk = pk)

      if request.method=="POST":
            form=CrearComentario(request.POST)
            if form.is_valid():
                  autor=User.objects.get(username=request.user) 
                  info=form.cleaned_data
                  comentario=info["comentario"]
                  comentario=Comentario(post=post, autor=autor, comentario=comentario)
                  comentario.save()
                  return HttpResponseRedirect(reverse("PostVista", args=[str(pk)]))
            else:
                  return render(request, "Blog/post.html", {"mensaje": "Error. Se ingresaron mal los datos"})
    
      else:
            form=CrearComentario()
            return render(request, "Blog/crearComentario.html", {"form": form, "post":post})

@login_required
def eliminarComentario(request, id):
    comentario=Comentario.objects.get(id=id)
    post=Post.objects.filter(comentarios=comentario.id)
    pk= post[0].id

    if comentario.autor==request.user:
          comentario.delete()
          return HttpResponseRedirect(reverse("PostVista", args=[str(pk)]))

# @login_required
# def editarComentario(request, id):
#       comentario=Comentario.objects.get(id=id)
#       if request.method=="POST":
#             form=CrearComentario(request.POST)
#             if form.is_valid():
#                   info=form.cleaned_data
#                   comentario=info["nombre"]
#                   comentario.save()
#                   post=Post.objects.filter(comentarios=comentario.id)
#                   pk= post[0].id
#                   comentarios=Comentario.objects.all()
#                   return HttpResponseRedirect(reverse("PostVista", args=[str(pk)]))
#             else:
#                   return render(request, "Blog/post.html", {"mensaje": "Error. Se ingresaron mal los datos"})
    
#       else:
#             form=CrearComentario(initial={"comentario":comentario.comentario})
#             return render(request, "Blog/editarComentario.html", {"form": form})
