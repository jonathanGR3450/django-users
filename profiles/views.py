from django.shortcuts import render
from django.views.generic import ListView, DetailView
from registration.models import Profile
from django.shortcuts import get_object_or_404

# Create your views here.
class ProfilesListView(ListView):
    model = Profile
    template_name = 'profiles/profile_list.html'
    paginate_by = 10

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profiles/profile_detail.html'

    # como en la url envio el username, no el pk del modelo, entonces me toca recuperarlo de esta forma
    def get_object(self):
        return get_object_or_404(Profile, user__username=self.kwargs['username'])