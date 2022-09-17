from django.urls import path
from Blog import views


urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('about/', views.about, name="About"),
    path ('crearPost/', views.crearPost, name="CrearPost"), 
    path('post/<int:pk>',views.postVista, name="PostVista"),
    path ('pages/', views.listaPosts, name="ListaPosts"),
    path('eliminarPost/<id>', views.eliminarPost, name="eliminarPost"),
    # path('editarPost/<id>', views.editarPost, name="editarPost"),
    path('like/<int:pk>', views.likeView, name="like_post"),


]