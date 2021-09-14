from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.base import Model
from django.db.models.deletion import SET_NULL
from django.db.models.query import QuerySet
from django.http.request import QueryDict


class Vezerlo(models.Model):
    nev = models.CharField(max_length=100)
    kod = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Vezerlő'
        verbose_name_plural = 'Vezerlők'

    def __str__(self):
        return f'{self.nev} ({self.kod})'


class Osztaly(models.Model):
    nev = models.CharField(max_length=50, default="-")
    kod = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = 'Osztály'
        verbose_name_plural = 'Osztályok'

    def __str__(self):
        return f'{self.nev} ({self.kod})'


class Felhasznalo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nev = models.CharField(max_length=100)
    osztaly = models.ForeignKey(Osztaly, on_delete=models.SET_NULL, null=True)
    kulsos = models.BooleanField(default=False)
    gyogy = models.BooleanField(default=False)
    felmentett = models.BooleanField(default=False)


    class Meta:
        verbose_name = 'Felhasználó'
        verbose_name_plural = 'Felhasználók'

    def __str__(self):
        return str(self.user) + f' ({self.nev})'

    def getuser(request):
        return Felhasznalo.objects.get(user=request.user)

    def jelentkezese(self):
        return Jelentkezes.objects.get(felhasznalo = self)

    def foglalkozasa(self):
        return self.jelentkezese().foglalkozas

    def akik_nem_jelentkeztek()->list:
        nevsor = []
        testnevelotanarok = Group.objects.get(name='testnevelotanar')
        for a_felhasznalo in Felhasznalo.objects.all():
            if Jelentkezes.objects.filter(felhasznalo=a_felhasznalo).count()==0 and testnevelotanarok not in a_felhasznalo.user.groups.all():
                nevsor.append(a_felhasznalo.nev)
        nevsor.sort()
        return nevsor

tipusnevek = (
    ('DSE','DSE'),
    ('nem DSE', 'nem DSE'),
)

tipuskodok = (
    ('dse','dse'),
    ('nemdse', 'nemdse'),
)

napok = (
    ('Hétfő','Hétfő'),
    ('Kedd','Kedd'),
    ('Szerda','Szerda'),
    ('Csütörtök','Csütörtök'),
    ('Péntek','Péntek'),
    ('Szombat','Szombat'),
    ('Vasárnap','Vasárnap'),
)

class Foglalkozas(models.Model):
    kod = models.CharField(max_length=20)
    letszam = models.IntegerField()
    tipus_nev = models.CharField(max_length=10, choices=tipusnevek, default='-')
    tipus_kod = models.CharField(max_length=10, choices=tipuskodok, default='-')
    nev = models.CharField(max_length=50)
    egyik_nap = models.CharField(max_length=10, choices=napok)
    egyik_mettol = models.DurationField()
    egyik_meddig = models.DurationField()
    egyik_tanar = models.CharField(max_length=100)
    bomlik = models.BooleanField(default=False)
    masik_nap = models.CharField(max_length=10, choices=napok, blank=True, null = True)
    masik_mettol = models.DurationField(blank=True, null=True)
    masik_meddig = models.DurationField(blank=True, null=True)
    masik_tanar = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Foglalkozás'
        verbose_name_plural = 'Foglalkozások'

    def __str__(self) -> str:
        if self.bomlik:
            return f"{self.nev}: ({self.egyik_tanar} és {self.masik_tanar}, {self.tipus_nev}), {self.egyik_nap}: {self.egyik_mettol} - { self.egyik_meddig } és {self.masik_nap}: {self.masik_mettol} - { self.masik_meddig }, {self.aktletszam()}/{self.letszam}"
        else:
            return f"{self.nev}: ({self.egyik_tanar}, {self.tipus_nev}), {self.egyik_nap}: {self.egyik_mettol} - { self.egyik_meddig }, {self.aktletszam()}/{self.letszam}"


    def jelentkezesei(self) -> QuerySet:
        return Jelentkezes.objects.filter(foglalkozas = self)

    def felhasznaloi(self) -> list: # -> list[Felhasznalo]:
        nevsor = map(lambda x: x.felhasznalo, Jelentkezes.objects.filter(foglalkozas = self))
        return sorted(nevsor, key = lambda fh : fh.nev)
    

    def aktletszam(self) -> int:
        return Jelentkezes.objects.filter(foglalkozas = self).count()

    def lista(szurestipus, request) -> list:
        lista = []
        foglalkozasok = Foglalkozas.objects.all() if szurestipus=='' else Foglalkozas.objects.filter(tipus_kod=szurestipus)
        for foglalkozas in foglalkozasok:
            lista.append({
                'nev': foglalkozas.nev,
                'kod': foglalkozas.kod,
                'maxletszam': foglalkozas.letszam,
                'tipus_nev': foglalkozas.tipus_nev,
                'tipus_kod': foglalkozas.tipus_kod,
                'bomlik': foglalkozas.bomlik,
                'egyik_tanar': foglalkozas.egyik_tanar,
                'egyik_nap': foglalkozas.egyik_nap,
                'egyik_mettol': timedelta2str(foglalkozas.egyik_mettol),
                'egyik_meddig': timedelta2str(foglalkozas.egyik_meddig),
                'masik_tanar': foglalkozas.masik_tanar,
                'masik_nap': foglalkozas.masik_nap,
                'masik_mettol': timedelta2str(foglalkozas.masik_mettol),
                'masik_meddig': timedelta2str(foglalkozas.masik_meddig),
                'aktletszam': foglalkozas.aktletszam(),
                'id': foglalkozas.id,
            })
        return lista


class Jelentkezes(models.Model):
    
    felhasznalo = models.ForeignKey(Felhasznalo, on_delete=models.CASCADE)
    foglalkozas = models.ForeignKey(Foglalkozas, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Jelentkezés'
        verbose_name_plural = 'Jelentkezések'

    def __str__(self) -> str:
        """Unicode representation of Jelentkezes."""
        return f"{self.felhasznalo.nev} -> {self.foglalkozas.nev} "



def timedelta2str(td):
    return f'{str(td.seconds//3600).zfill(2)}:{str(td.seconds//60%60).zfill(2)}' if td != None else None
