from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(null=True, blank=True, upload_to="imagenesPerfil")
    descripcion = models.CharField(max_length=500, blank=True)
    pagina_web=models.URLField()

    def __str__(self):
        return f'Perfil de {self.user.username}'
    
    @receiver(post_save, sender=User)
    def create_perfil(sender, instance, created, **kwargs):
        if created:
            Perfil.objects.create(user=instance)
