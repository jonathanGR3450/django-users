from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from .models import Page
from .forms import PagesForm

# un mixin es una clase que tiene un comportamineto, la cual puede ser heredada a otras clases
# class StaffRequiredPage(object):
#     @method_decorator(staff_member_required)
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)

# Create your views here.
class PagesListView(ListView):
    model = Page

class PageDetailView(DetailView):
    model = Page

@method_decorator(staff_member_required, name='dispatch')
class PageCreate(CreateView):
    model = Page
    form_class = PagesForm
    success_url = reverse_lazy('pages:pages')
    
@method_decorator(staff_member_required, name='dispatch')
class PageUpdateView(UpdateView):
    model = Page
    form_class = PagesForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class PageDeleteView(DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')
    # video 66
