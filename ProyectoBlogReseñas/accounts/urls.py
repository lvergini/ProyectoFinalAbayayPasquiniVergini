from django.urls import path
from accounts import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.login_request, name='login'),
    path('register/', views.register, name="register"),
    # path('logout/', LogoutView.as_view(template_name="accounts/logout.html"), name="logout"),
    # path('profile/<int:pk>',views.profile,name="profile"),
    # path('editarPerfil/', views.editarPerfil, name="editarPerfil"),
]