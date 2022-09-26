from django.urls import path
from Libros import views

urlpatterns = [
    path('autorCrear/', views.autorCrear, name="AutorCrear"),
    path('eliminarAutor/<id>', views.eliminarAutor, name='EliminarAutor'),
    path('editarAutor/<id>', views.editarAutor, name='EditarAutor'),
    path('listaAutores/', views.listaAutores, name='ListaAutores'),
    path('autorVista/<id>/', views.autorVista, name="AutorVista"),
    path('editorialCrear/', views.editorialCrear, name="EditorialCrear"),
    path('listaEditoriales/', views.listaEditoriales, name='ListaEditoriales'),
    path('editarEditorial/<id>', views.editarEditorial, name='EditarEditorial'),
    path('eliminarEditorial/<id>', views.eliminarEditorial, name='EliminarEditorial'),
    path('libroCrear/', views.libroCrear, name="LibroCrear"),
    path('editarLibro/<id>', views.editarLibro, name='EditarLibro'),
    path('eliminarLibro/<id>', views.eliminarLibro, name='EliminarLibro'),
    path('busquedaLibro/', views.busquedaLibro, name='BusquedaLibro'),
    path('buscarLibro/', views.buscarLibro, name='buscarLibro'),
    path('libroVista/<id>/', views.libroVista, name="LibroVista"),




]