from django.core.urlresolvers import reverse
from django.shortcuts import render
from serwis.models import Kontrahent
from serwis.models import Oddzial
from django.views.generic import ListView
from django.views.generic import CreateView
# Create your views here.


class ListKontrahentView(ListView):
    model = Kontrahent
    template_name = 'kontrahent_list.html'

class CreateKontrahentView(CreateView):
    model = Kontrahent
    template_name = 'kontrahent_edit.html'
    fields = ('nazwa', 'nip', 'ulica', 'kod', 'miasto', )

    def get_success_url(self):
        return reverse('kontrahent-list')

class ListOddzialView(ListView):
    model = Oddzial
    template_name = 'oddzial_list.html'

class CreateOddzialView(CreateView):
    model = Oddzial
    template_name = 'oddzial_edit.html'
    fields = ('nazwa', 'mpk', 'kontrahent')

    def get_success_url(self):
        return reverse('oddzial-list')
