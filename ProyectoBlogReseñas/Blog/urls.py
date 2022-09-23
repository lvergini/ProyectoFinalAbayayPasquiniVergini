from django.urls import path
from Blog import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('about/', views.about, name="About"),
    path ('crearPost/', views.crearPost, name="CrearPost"), 
    path('post/<int:pk>',views.postVista, name="PostVista"),
    path ('pages/', views.listaPosts, name="ListaPosts"),
    path('eliminarPost/<id>', views.eliminarPost, name="eliminarPost"),
    path('busquedaPost/', views.busquedaPost, name='BusquedaPost'),
    path('buscarPost/', views.buscarPost, name='buscarPost'),
    path('editarPost/<id>', views.editarPost, name="editarPost"),
    path('crearCategoria/', views.crearCategoria, name="CrearCategoria"),
    path('categoria/<str:cat>/', views.categoriaPosts, name="CategoriaPosts"),
    path('listaCategorias/', views.listaCategorias, name="listaCategorias"),
    path ('post/<int:pk>/crearComentario/', views.crearComentario, name="CrearComentario"),
    path('eliminarComentario/<id>', views.eliminarComentario, name='EliminarComentario'),
    #path('editarComentario/<id>', views.editarComentario, name='EditarComentario'),

    path('like/<int:pk>', views.likeView, name="like_post"),


]