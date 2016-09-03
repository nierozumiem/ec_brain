from django.core.urlresolvers import reverse
from django.shortcuts import render
from django_tables2 import RequestConfig
from serwis.models import Kontrahent
from serwis.models import Oddzial
from serwis.models import Urzadzenie
from serwis.models import TypUrzadzenia
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from .tables import KontrahenciTable
from .tables import OddzialyTable
from .tables import TypyUrzadzenTable
from .tables import UrzadzeniaTable
# Create your views here.


# class ListKontrahentView(ListView):
#     model = Kontrahent
#     template_name = 'kontrahent_list.html'

def home(request):
    return render(request, 'home.html')

def kontrahenci(request):
    table = KontrahenciTable(Kontrahent.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'kontrahent_list_table.html', {'kontrahenci': table})

class CreateKontrahentView(CreateView):
    model = Kontrahent
    template_name = 'kontrahent_edit.html'
    fields = ('nazwa', 'nip', 'ulica', 'kod', 'miasto', )

    def get_success_url(self):
        return reverse('kontrahent_list')
    
    def get_context_data(self, **kwargs):
            context = super(CreateKontrahentView, self).get_context_data(**kwargs)
            context['action'] = reverse('kontrahent_new')
            return context

class UpdateKontrahentView(UpdateView):
    model = Kontrahent
    template_name = 'kontrahent_edit.html'
    fields = ('nazwa', 'nip', 'ulica', 'kod', 'miasto', )

    def get_success_url(self):
        return reverse('kontrahent-list')

    def get_context_data(self, **kwargs):
            context = super(UpdateKontrahentView, self).get_context_data(**kwargs)
            context['action'] = reverse('kontrahent_edit', kwargs={'pk': self.get_object().id})
            return context

# class ListOddzialView(ListView):
#     model = Oddzial
#     template_name = 'oddzial_list.html'

def oddzialy(request):
    table = OddzialyTable(Oddzial.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'oddzial_list_table.html', {'oddzialy': table})


class CreateOddzialView(CreateView):
    model = Oddzial
    template_name = 'oddzial_edit.html'
    fields = ('nazwa', 'mpk', 'kontrahent')

    def get_success_url(self):
        return reverse('oddzial_list')

class UpdateOddzialView(UpdateView):
    model = Oddzial
    template_name = 'oddzial_edit.html'
    fields = ('nazwa', 'mpk', 'kontrahent')

    def get_success_url(self):
        return reverse('oddzial_list')

    def get_context_data(self, **kwargs):
            context = super(UpdateOddzialView, self).get_context_data(**kwargs)
            context['action'] = reverse('oddzial_edit', kwargs={'pk': self.get_object().id})
            return context

# class ListUrzadzenieView(ListView):
#     model = Urzadzenie
#     template_name = 'urzadzenie_list.html'

def urzadzenia(request):
    table = UrzadzeniaTable(Urzadzenie.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'urzadzenie_list_table.html', {'urzadzenia': table})

class CreateUrzadzenieView(CreateView):
    model = Urzadzenie
    template_name = 'urzadzenie_edit.html'
    fields = ('producent', 'typ', 'moc', 'rodzaj_czynnika', 'miejsce_montazu', 'koniec_gwarancji', 'multi', 'ile_multi', 'strategiczny', 'uwagi', 'numer_seryjny', 'typ_urzadzenia', 'oddzial')

    def get_success_url(self):
        return reverse('urzadzenie_list')

class UpdateUrzadzenieView(UpdateView):
    model = Urzadzenie
    template_name = 'urzadzenie_edit.html'
    fields = ('producent', 'typ', 'moc', 'rodzaj_czynnika', 'miejsce_montazu', 'koniec_gwarancji', 'multi', 'ile_multi', 'strategiczny', 'uwagi', 'numer_seryjny', 'typ_urzadzenia', 'oddzial')

    def get_success_url(self):
        return reverse('urzadzenie_list')

    def get_context_data(self, **kwargs):
            context = super(UpdateUrzadzenieView, self).get_context_data(**kwargs)
            context['action'] = reverse('urzadzenie_edit', kwargs={'pk': self.get_object().id})
            return context


def typy_urzadzen(request):
    table = TypyUrzadzenTable(TypUrzadzenia.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'typ_urzadzenia_list_table.html', {'typy_urzadzen': table})

class CreateTypUrzadzeniaView(CreateView):
    model = TypUrzadzenia
    template_name = 'typ_urzadzenia_edit.html'
    fields = ('typ', )

    def get_success_url(self):
        return reverse('typ_urzadzenia_list')

class UpdateTypUrzadzeniaView(UpdateView):
    model = TypUrzadzenia
    template_name = 'typ_urzadzenia_edit.html'
    fields = ('typ', )

    def get_success_url(self):
        return reverse('typ_urzadzenia_list')

    def get_context_data(self, **kwargs):
            context = super(UpdateTypUrzadzeniaView, self).get_context_data(**kwargs)
            context['action'] = reverse('typ_urzadzenia_edit', kwargs={'pk': self.get_object().id})
            return context
