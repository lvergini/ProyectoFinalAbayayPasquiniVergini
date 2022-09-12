from django.urls import path
from Blog import views


urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('about/', views.about, name="About"),
    path ('crearPost/', views.crearPost, name="CrearPost"), 

]