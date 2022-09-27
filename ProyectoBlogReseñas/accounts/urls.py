from django.urls import path
from accounts import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.login_request, name='login'),
    path('signup/', views.signup, name="signup"),
    path('profile/<int:pk>',views.profile,name="profile"),
    path('editarPerfil/', views.editarPerfil, name="editarPerfil"),
    path('logout/', LogoutView.as_view(template_name="accounts/logout.html"), name="logout"),
    path('conversacion/<str:usu>/', views.conversacion, name="Conversacion"),
    path('messagesUsu/<str:usu>/', views.mensajeAUsuario, name="messagesUsu")
   
]