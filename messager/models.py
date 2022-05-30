from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import m2m_changed

# Create your models here.
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

class ThreadManager(models.Manager):
    def find(self, user1, user2):
        queryset = self.filter(user=user1).filter(user=user2)
        if len(queryset) > 0:
            return queryset[0]
        return None
    
    def find_or_create(self, user1, user2):
        thread = self.find(user1, user2)
        if thread is None:
            # creo el thread
            thread = Thread.objects.create()
            thread.user.add(user1, user2)
        return thread

# hacer la signal para que cuando se agrege un usuario al mensaje, validar que solo esten dos usuarios
class Thread(models.Model):
    user = models.ManyToManyField(User, related_name='threads')
    messages = models.ManyToManyField(Message)
    updated = models.DateTimeField(auto_now=True)
    objects = ThreadManager()

    class Meta:
        ordering = ['-updated']

# signal para validar si el usurio que envio el mensaje es parte del hilo
def message_change(sender, **kwargs):
    instance = kwargs.pop('instance', None)
    action = kwargs.pop('action', None)
    pk_set = kwargs.pop('pk_set', None)
    false_msg = set()
    if action == "pre_add":
        for msg_pk in pk_set:
            msg = Message.objects.get(pk=msg_pk)
            if msg.user not in instance.user.all():
                false_msg.add(msg_pk)
    
    # eliminamos los mensajes fake de pk_set
    pk_set.difference_update(false_msg)
    instance.save()
            

m2m_changed.connect(message_change, sender=Thread.messages.through)