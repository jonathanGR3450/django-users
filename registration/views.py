from registration.models import Profile
from .forms import EmailUpdateForm, UserCreationFormWithEmail
from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django import forms
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from registration.forms import ProfileUpdateForm


# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationFormWithEmail
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse_lazy('login') + '?ok'

    # modificamos el formulario generico para crear usuarios, lo hacemos en tiempo de ejecucion para no perder las validaciones
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Nombre de usuario'})
        form.fields['email'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Direccion de correo'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Contrasena'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Confirmar contrasena'})
        return form

@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
    form_class = ProfileUpdateForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_form.html'

    # forma de obtener el objeto que se va a editar desde la vista updated
    def get_object(self):
        print(self.request.user)
        profile, create = Profile.objects.get_or_create(user=self.request.user)
        return profile

class EmailUpdated(UpdateView):
    form_class = EmailUpdateForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/form_email_update.html'

    def get_object(self):
        return self.request.user
    
    def get_form(self, form_class=None):
        form = super(EmailUpdated, self).get_form()
        form.fields['email'].widget = forms.EmailInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Correo electronico'})
        return form
