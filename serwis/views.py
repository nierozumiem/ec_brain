from django.core.urlresolvers import reverse
from django.shortcuts import render
from serwis.models import Kontrahent
from serwis.models import Oddzial
from serwis.models import Urzadzenie
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView

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
    
    def get_context_data(self, **kwargs):
            context = super(CreateKontrahentView, self).get_context_data(**kwargs)
            context['action'] = reverse('kontrahent-new')
            return context

class UpdateKontrahentView(UpdateView):
    model = Kontrahent
    template_name = 'kontrahent_edit.html'
    fields = ('nazwa', 'nip', 'ulica', 'kod', 'miasto', )

    def get_success_url(self):
        return reverse('kontrahent-list')

    def get_context_data(self, **kwargs):
            context = super(UpdateKontrahentView, self).get_context_data(**kwargs)
            context['action'] = reverse('kontrahent-edit', kwargs={'pk': self.get_object().id})
            return context

class ListOddzialView(ListView):
    model = Oddzial
    template_name = 'oddzial_list.html'

class CreateOddzialView(CreateView):
    model = Oddzial
    template_name = 'oddzial_edit.html'
    fields = ('nazwa', 'mpk', 'kontrahent')

    def get_success_url(self):
        return reverse('oddzial-list')

class UpdateOddzialView(UpdateView):
    model = Oddzial
    template_name = 'oddzial_edit.html'
    fields = ('nazwa', 'mpk', 'kontrahent')

    def get_success_url(self):
        return reverse('oddzial-list')

    def get_context_data(self, **kwargs):
            context = super(UpdateOddzialView, self).get_context_data(**kwargs)
            context['action'] = reverse('oddzial-edit', kwargs={'pk': self.get_object().id})
            return context

class ListUrzadzenieView(ListView):
    model = Urzadzenie
    template_name = 'urzadzenie_list.html'

class CreateUrzadzenieView(CreateView):
    model = Urzadzenie
    template_name = 'urzadzenie_edit.html'
    fields = ('producent', 'typ', 'moc', 'rodzaj_czynnika', 'miejsce_montazu', 'koniec_gwarancji', 'multi', 'ile_multi', 'strategiczny', 'uwagi', 'numer_seryjny', 'typ_urzadzenia', 'oddzial')

    def get_success_url(self):
        return reverse('oddzial-list')
