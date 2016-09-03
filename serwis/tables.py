import django_tables2 as tables
from django_tables2.utils import A
from .models import Kontrahent
from .models import Oddzial
from .models import TypUrzadzenia
from .models import Urzadzenie

class KontrahenciTable(tables.Table):
    class Meta:
        model = Kontrahent
        attrs = {'class': 'paleblue'}

    edit = tables.LinkColumn('kontrahent_edit', args=[A('pk')], text='edycja',orderable=False)

class OddzialyTable(tables.Table):
    class Meta:
        model = Oddzial
        attrs = {'class': 'paleblue'}

    edit = tables.LinkColumn('oddzial_edit', args=[A('pk')], text='edycja',orderable=False)

class TypyUrzadzenTable(tables.Table):
    class Meta:
        model = TypUrzadzenia
        attrs = {'class': 'paleblue'}

    edit = tables.LinkColumn('typ_urzadzenia_edit', args=[A('pk')], text='edycja',orderable=False)

class UrzadzeniaTable(tables.Table):
    class Meta:
        model = Urzadzenie
        attrs = {'class': 'paleblue'}

    edit = tables.LinkColumn('urzadzenie_edit', args=[A('pk')], text='edycja',orderable=False)
