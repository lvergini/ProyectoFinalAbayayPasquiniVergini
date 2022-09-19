from django.shortcuts import render
from django.http import HttpResponse
from Libros.forms import *
from Libros.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from Blog.models import Post

@login_required
def autorCrear(request):
    if request.method=="POST":
        miFormulario=AutorFormulario(request.POST)
        if miFormulario.is_valid():
            info=miFormulario.cleaned_data
            nombre=info["nombre"]
            apellido=info["apellido"]
            autor=Autor(nombre=nombre, apellido=apellido)
            autorEnBase=Autor.objects.filter(nombre=nombre, apellido=apellido)
            if len(autorEnBase)!=0:
                return render(request, "libros/autorCrear.html", {"mensaje": f"Ya está cargado en la base el autor {nombre} {apellido}", "formulario":miFormulario})
            else: 
                autor.save()
            return render(request, "Blog/inicio.html", {"mensaje": f"Se creó el autor {nombre} {apellido}"})
        else:
            return render(request, "libros/autorCrear.html", {"mensaje": "Error. Se ingresaron mal los datos"})
    
    else:
        miFormulario=AutorFormulario()
        return render(request, "Libros/autorCrear.html", {"formulario": miFormulario})

def listaAutores(request):
    autores=Autor.objects.all()
    # for autor in autores:
    #     if len(autor.libro)!=0:
    #         libro_posts=Post.objects.filter(libro=autor.libro)
    #         if len(libro_posts)!=0:
    #             return render(request, "Libro/categoria.html", {"cat":cat.title().replace('-', ' '), "categoria_posts":categoria_posts} )
    #     else:
    #         return render(request, "Blog/categoria.html", {"cat":cat.title().replace('-', ' '), "mensaje": f"Todavía no fue creada la categoría {cat}"} )
    return render(request, "libros/listaAutores.html", {"autores":autores})


@staff_member_required
def eliminarAutor(request, id):
    autor=Autor.objects.get(id=id)
    autor.delete()
    autores=Autor.objects.all()
    return render(request, "libros/listaAutores.html", {"autores":autores})

@staff_member_required
def editarAutor(request, id):
    autor=Autor.objects.get(id=id)
    if request.method=="POST":
        form=AutorFormulario(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            autor.nombre=info["nombre"]
            autor.apellido=info["apellido"]
            autor.save()
            autores=Autor.objects.all()
            return render(request, "libros/listaAutores.html", {"autores":autores})
    
    else:
        form=AutorFormulario(initial={"nombre":autor.nombre, "apellido":autor.apellido})
        return render(request, "libros/editarAutor.html", {"formulario":form, "nombre_autor":autor.nombre, "id":autor.id})

@login_required
def editorialCrear(request):
    if request.method=="POST":
        miFormulario=EditorialFormulario(request.POST)
        if miFormulario.is_valid():
            info=miFormulario.cleaned_data
            nombre=info["nombre"]
            email=info["email"]
            editorial=Editorial(nombre=nombre, email=email)
            editorialEnBase=Editorial.objects.filter(nombre=nombre)
            if len(editorialEnBase)!=0:
                return render(request, "libros/editorialCrear.html", {"mensaje": f"Ya está cargada en la base la editorial {nombre}", "formulario":miFormulario})
            else:
                editorial.save()
            return render(request, "Blog/inicio.html", {"mensaje": f"Se creó la editorial {nombre}"})
        else:
            return render(request, "libros/editorialCrear.html", {"mensaje": "Error. Se ingresaron mal los datos"})
    
    else:
        miFormulario=EditorialFormulario()
        return render(request, "libros/editorialCrear.html", {"formulario": miFormulario})

@login_required
def libroCrear(request):
    if request.method=="POST":
        miFormulario=LibroFormulario(request.POST, request.FILES)
        if miFormulario.is_valid():
            info=miFormulario.cleaned_data
            titulo=info["titulo"]
            isbn=info["isbn"]
            fecha_publicacion= info["fecha_publicacion"]
            autor= Autor.objects.get(pk = info["autor"].id)
            editorial= Editorial.objects.get(pk = info["editorial"].id)
            imagen=info["imagen"]
            libro = Libro(titulo = titulo, isbn = isbn, fecha_publicacion = fecha_publicacion , autor= autor, editorial = editorial, imagen=imagen)
            libroEnBase=Libro.objects.filter(titulo=titulo, autor=autor)
            if len(libroEnBase)!=0:
                return render(request, "libros/libroCrear.html", {"mensaje": f"Ya está cargado en la base el libro {titulo}, del autor {autor}", "formulario":miFormulario})
            else: 
                libro.save()
            return render(request, "Blog/inicio.html", {"mensaje": f"Se creó el libro {titulo}"})
        else:
            return render(request, "AppLibros/inicio.html", {"mensaje": "Error. Se ingresaron mal los datos"})
    
    else:
        miFormulario=LibroFormulario()
        return render(request, "libros/libroCrear.html", {"formulario": miFormulario})

def busquedaLibro(request):
    return render(request, "libros/busquedaLibro.html")

def buscarLibro(request):
    if request.GET["autor"] and request.GET["titulo"]:
        autor=request.GET["autor"]
        titulo=request.GET["titulo"]
        autores=Autor.objects.filter(apellido__icontains=autor)
        libros=Libro.objects.filter(titulo__icontains=titulo, autor__apellido__icontains=autor)
        if len(autores)==0:
            return render(request, "libros/resultadoLibros.html", {"mensajeLibro": f'No hay ningún autor de apellido "{autor}"'})
        elif len(libros)!=0:
            return render(request, "libros/resultadoLibros.html", {"libros":libros})
        else:
            return render(request, "libros/resultadoLibros.html", {"mensajeLibro": f'No hay libros del autor "{autor}" que contengan en su título "{titulo}"'})
    
    if request.GET["autor"]:
        autor=request.GET["autor"]
        libros=Libro.objects.filter(autor__apellido__icontains=autor)
        autores=Autor.objects.filter(apellido__icontains=autor)
        if len(autores)==0:
            return render(request, "libros/resultadoLibros.html", {"mensajeLibro": f'No hay ningún autor de apellido "{autor}"'})
        elif len(libros)!=0:
            return render(request, "libros/resultadoLibros.html", {"libros":libros})
        else:
            return render(request, "libros/resultadoLibros.html", {"mensaje": f'No hay libros del autor "{autor}"'})
    
    elif request.GET["titulo"]:
        titulo=request.GET["titulo"]
        libros=Libro.objects.filter(titulo__icontains=titulo)
        if len(libros)!=0:
            return render(request, "libros/resultadoLibros.html", {"libros":libros})
        else:
            return render(request, "libros/resultadoLibros.html", {"mensaje": f'No hay libros que contengan en su título "{titulo}"'})
    else:
        return render(request, "libros/busquedaLibro.html", {"mensaje": "¡No enviaste datos!"})

def autorVista(request, id):
    autor=Autor.objects.filter(id=id)
    autor=autor[0]
      #if len(autor.libro)!=0:
    libros=Libro.objects.filter(autor=autor)
    if len(libros)!=0:
        for libro in libros:
            libro_posts=Post.objects.filter(libro=libro)
            return render(request, "libros/autorVista.html",  {"id":id, "autor": autor, "libros":libros, "libro_posts":libro_posts} )
    else:
        return render(request, "libros/autorVista.html",  {"id":id, "autor": autor, "libros":libros} )

