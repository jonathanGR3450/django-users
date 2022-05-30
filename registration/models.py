from signal import signal
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# eliminamos la imagen anterior y solo guardamos la actual
def custom_upload_to(instance, filename):
    old_img = Profile.objects.get(pk=instance.pk)
    old_img.avatar.delete()
    return 'profiles/' + filename

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, verbose_name='Usuario')
    avatar = models.ImageField(blank=True, null=True, upload_to=custom_upload_to, verbose_name='Avatar')
    bio = models.TextField(null=True, blank=True, verbose_name='Biografia')
    link = models.URLField(blank=True, null=True, max_length=200, verbose_name='Enlace')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion', null=True)
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha actualizacion', null=True)

    class Meta:
        ordering = ('user__username',)

# signal, es un disparador que sirve para ejecutar acciones, antes durante y despues 
@receiver(post_save, sender=User)
def ensure_profile_user(sender, instance, **kwargs):
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=instance)
        # print('se creo un perfil para este usuario')
