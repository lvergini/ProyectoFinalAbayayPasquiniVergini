from django.urls import path
from Blog import views


urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('about/', views.about, name="About"),
    path ('crearPost/', views.crearPost, name="CrearPost"), 
    path('verPost/<int:pk>',views.verPost, name="verPost"),
    path ('pages/', views.pages, name="pages"),
    path('eliminarPost/<id>', views.eliminarPost, name="eliminarPost"),
    # path('editarPost/<id>', views.editarPost, name="editarPost"),

]