from django.shortcuts import render

# Create your views here.
def inicio(request):
      return render(request, "Blog/inicio.html")

def about(request):
      return render(request, "Blog/about.html")

def crearPost(request):
#     if request.method=="POST":
#         form=CrearBlog(request.POST, request.FILES)
#         if form.is_valid():
#             info=form.cleaned_data
#             titulo= info['titulo']
#             subtitulo= info['subtitulo']
#             libro= info['libro']
#             imagen= info['imagen']
#             cuerpo=info['cuerpo']
#             autor=request.user
#             blog=Blog(titulo=titulo, subtitulo=subtitulo, libro=libro, imagen=imagen, cuerpo=cuerpo, autor=autor)
      return render(request, "Blog/CrearBlog.html")

