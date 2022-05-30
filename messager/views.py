from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Message, Thread
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import Http404, JsonResponse
from django.urls import reverse_lazy
from django.shortcuts import redirect

# Create your views here.
@method_decorator(login_required, name='dispatch')
class ThreadListView(ListView):
    model = Thread

    def get_queryset(self):
        queryset = super().get_queryset()
        print(queryset.filter(user=self.request.user))
        return queryset.filter(user=self.request.user)
    
@method_decorator(login_required, name='dispatch')
class ThreadDetailView(DetailView):
    model = Thread

    def get_object(self):
        thread = super().get_object()
        # validar que el usuario autenticado este dentro de los usuarios del hilo
        if self.request.user not in thread.user.all():
            raise Http404()
        return thread

@login_required
def send_message_to_thread(request, pk):
    # crear un mensaje de ese usuario
    content = request.GET.get('content', None)
    # recuperamos el hilo
    thread = get_object_or_404(Thread, pk=pk)
    msg = Message.objects.create(user=request.user, content=content)
    thread.messages.add(msg)

    html = '<div class="mine mb-3"><small><i>Hace unos segundos</i></small><br>{}</div>'.format(content)
    first = False
    if len(thread.messages.all()) == 1:
        first = True
    
    return JsonResponse({
        'created': True,
        'content': content,
        'message': 'Se creo envio el mensaje exitosamente',
        'html': html,
        'first': first
})

def create_thread_for_user(request, pk):
    # obtengo el usuario
    user = get_object_or_404(User, pk=pk)
    print(user, pk, request.user)
    thread = Thread.objects.find_or_create(request.user, user)
    return redirect(reverse_lazy("messager:detail", args=[thread.pk]))