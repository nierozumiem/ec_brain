"""ec_brain URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


import serwis.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^kontrahent-list$', serwis.views.ListKontrahentView.as_view(), name='kontrahent-list',),
    url(r'^kontrahent-new$', serwis.views.CreateKontrahentView.as_view(), name='kontrahent-new',),
    url(r'^kontrahent-edit/(?P<pk>\d+)/$', serwis.views.UpdateKontrahentView.as_view(), name='kontrahent-edit',),
    url(r'^oddzial-list$', serwis.views.ListOddzialView.as_view(), name='oddzial-list',),
    url(r'^oddzial-new$', serwis.views.CreateOddzialView.as_view(), name='oddzial-new',),
    url(r'^oddzial-edit/(?P<pk>\d+)/$', serwis.views.UpdateOddzialView.as_view(), name='oddzial-edit',),
    url(r'^urzadzenie-list$', serwis.views.ListUrzadzenieView.as_view(), name='urzadzenie-list',),
    url(r'^urzadzenie-new$', serwis.views.CreateUrzadzenieView.as_view(), name='urzadzenie-new',),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

