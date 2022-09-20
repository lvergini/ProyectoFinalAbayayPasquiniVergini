from django.urls import path
from Libros import views

urlpatterns = [
    path('autorCrear/', views.autorCrear, name="AutorCrear"),
    path('eliminarAutor/<id>', views.eliminarAutor, name='EliminarAutor'),
    path('editarAutor/<id>', views.editarAutor, name='EditarAutor'),
    path('listaAutores/', views.listaAutores, name='ListaAutores'),
    path('autorVista/<id>/', views.autorVista, name="AutorVista"),


    path('editorialCrear/', views.editorialCrear, name="EditorialCrear"),
    path('libroCrear/', views.libroCrear, name="LibroCrear"),
    path('busquedaLibro/', views.busquedaLibro, name='BusquedaLibro'),
    path('buscarLibro/', views.buscarLibro, name='buscarLibro'),
    path('libroVista/<id>/', views.libroVista, name="LibroVista"),




]