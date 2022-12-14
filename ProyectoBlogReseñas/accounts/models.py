from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from ckeditor.fields import RichTextField
from django.utils import timezone

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(default="default.jpg", upload_to="imagenesPerfil")
    descripcion = RichTextField(max_length=6000, blank=True)
    pagina_web=models.URLField()
    profesion=models.CharField(max_length=60, null=True, blank=True)
    pais=models.CharField(max_length=60, null=True, blank=True)
    instagram=models.URLField(null=True, blank=True)
    linkedin=models.URLField(null=True, blank=True)


    def __str__(self):
        return f'Perfil de {self.user.username}'
    
    @receiver(post_save, sender=User)
    def create_perfil(sender, instance, created, **kwargs):
        if created:
            Perfil.objects.create(user=instance)
            
class Mensaje(models.Model):
    emisor =   models.ForeignKey(User, related_name="emisor_mensaje",on_delete=models.CASCADE)
    receptor = models.ForeignKey(User, related_name="receptor_mensaje", on_delete=models.CASCADE)
    texto = models.CharField(max_length=140)
    leido = models.BooleanField
    fecha = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["fecha"]

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        self.fecha = timezone.now()
        return super(Mensaje, self).save(*args, **kwargs)
    
    def __str__(self):
        return f'{self.emisor.username} a {self.receptor.username}'