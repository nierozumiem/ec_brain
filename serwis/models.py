from django.db import models

# Create your models here.
class Kontrahent(models.Model):
    
    nazwa = models.CharField(
        max_length=255,
    )
    nip = models.CharField(
        max_length=255,
    )
    ulica = models.CharField(
        max_length=255,
    )
    kod = models.CharField(
        max_length=255,
    )
    miasto = models.CharField(
        max_length=255
    )

    def __str__(self):

        return self.nazwa

class Oddzial(models.Model):

    nazwa = models.CharField(
        max_length=255,
    )
    mpk = models.CharField(
        max_length=255
    )
    kontrahent = models.ForeignKey(
        'Kontrahent',
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return self.nazwa

class TypUrzadzenia(models.Model):
    
    typ = models.CharField(
        max_length=255,
    )

    def __str__(self):

        return self.typ

class Urzadzenie(models.Model):
    
    RODZAJE_CZYNNIKA = (
        ('R410', 'R 410'),
        ('R128', 'R 128'),
        ('R312', 'R 312'),
        ('R234', 'R 234'),
    )
    TAK_NIE = (
        ('1', 'TAK'),
        ('0', 'NIE'),
    )
    producent = models.CharField(
        max_length=255,
    )
    typ = models.CharField(
        max_length=255,
    )
    moc = models.DecimalField(
        max_digits=6,
        decimal_places=1,
    )
    rodzaj_czynnika = models.CharField(
        max_length=255,
        choices=RODZAJE_CZYNNIKA,
        default='R410',
    )
    miejsce_montazu = models.CharField(
        max_length=255,
    )
    koniec_gwarancji = models.DateField()
    multi = models.IntegerField(
        choices=TAK_NIE
    )
    ile_multi = models.PositiveSmallIntegerField()
    strategiczny = models.IntegerField(
        choices=TAK_NIE
    )
    uwagi = models.TextField()
    numer_seryjny = models.CharField(
        max_length=255,
    )
    typ_urzadzenia = models.ForeignKey(
        'TypUrzadzenia',
        on_delete=models.PROTECT,
    )
    oddzial = models.ForeignKey(
        'Oddzial',
        on_delete=models.PROTECT,
    )

    def __str__(self):
        
        return ' '.join([
            self.producent,
            self.typ,
        ])


class Przeglad(models.Model):

    data = models.DateField()
    ilosc_czynnika = models.DecimalField(
        max_digits=8,
        decimal_places=2,
    )
    dzialajace = models.BinaryField()
    uwagi = models.TextField()
    urzadzenie = models.ForeignKey(
        'Urzadzenie',
        on_delete=models.PROTECT
    )

    def __str__(self):
    
        return self.data

class Czesc(models.Model):
    
    nazwa = models.CharField(
        max_length=255,
    )

    def __str__(self):
        return self.nazwa

class WZ(models.Model):
    
    numer = models.CharField(
        max_length=255,
    )
    ilosc = models.DecimalField(
        max_digits=8,
        decimal_places=2,
    )
    czesc = models.ForeignKey(
        'Czesc',
        on_delete=models.PROTECT
    )

    def __str__(self):
        return ' '.join([
            self.czesc.parent__nazwa
        ])


class Naprawa(models.Model):    
    STATUSY = (
        ('OPEN', 'w trakcie'),
        ('CLOSED', 'zakonczona'),
    )
    opis = models.TextField()
    status = models.CharField(
        max_length = 255,
        choices=STATUSY,
    )
    data_rozpoczecia = models.DateField()
    data_zakonczenia = models.DateField()

    def __str__(self):
        return ' '.join([
            'data rozpoczęcia',
            self.data_rozpoczecia
        ])
