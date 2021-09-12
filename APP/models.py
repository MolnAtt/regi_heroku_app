from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.base import Model
from django.db.models.deletion import SET_NULL
from django.db.models.query import QuerySet
from django.http.request import QueryDict


class Osztaly(models.Model):
    nev = models.CharField(max_length=10)
    kod = models.CharField(max_length=10)
    
    class Meta:
        verbose_name = 'Osztály'
        verbose_name_plural = 'Osztályok'

    def __str__(self):
        return self.nev


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
        testnevelotanarok = Group.objects.get(name='testnevelotanarok')
        for a_felhasznalo in Felhasznalo.objects.all():
            if Jelentkezes.objects.filter(felhasznalo=a_felhasznalo).count()==0 and testnevelotanarok not in a_felhasznalo.user.groups.all():
                nevsor.append(a_felhasznalo.nev)
        nevsor.sort()
        return nevsor


class Tipus(models.Model):
    nev = models.CharField(max_length=50)
    kod = models.CharField(max_length=8)

    class Meta:
        verbose_name = 'Típus'
        verbose_name_plural = 'Típusok'

    def __str__(self) -> str:
        return f"{self.nev} ({self.kod})"


class Nap(models.Model):
    nev = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Nap'
        verbose_name_plural = 'Napok'

    def __str__(self) -> str:
        return self.nev


class Foglalkozas(models.Model):
    nev = models.CharField(max_length=50)
    kod = models.CharField(max_length=20)
    letszam = models.IntegerField()    
    tipus = models.ForeignKey(Tipus, on_delete=models.CASCADE, null=True)
    nap = models.ForeignKey(Nap, on_delete=models.CASCADE, null=True)
    mettol = models.DurationField()
    meddig = models.DurationField()
    tanar = models.ForeignKey(Felhasznalo, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Foglalkozás'
        verbose_name_plural = 'Foglalkozások'

    def __str__(self) -> str:
        return f"{self.nev}: ({self.tanar}, {self.tipus}), {self.nap}: {self.mettol} - { self.meddig }, {self.aktletszam()}/{self.letszam}"
    
    def jelentkezesei(self) -> QuerySet:
        return Jelentkezes.objects.filter(foglalkozas = self)

    def nevsora(self) -> list:
        nevsor = list(map(lambda x: x.felhasznalo.nev , Jelentkezes.objects.filter(foglalkozas = self)))
        nevsor.sort()
        return nevsor
    

    def aktletszam(self) -> int:
        return Jelentkezes.objects.filter(foglalkozas = self).count()

    def lista(szurestipus, request) -> list:
        lista = []
        foglalkozasok = Foglalkozas.objects.all() if szurestipus=='' else Foglalkozas.objects.filter(tipus=Tipus.objects.get(kod=szurestipus))
        for foglalkozas in foglalkozasok:
            lista.append({
                'nev': foglalkozas.nev,
                'kod': foglalkozas.kod,
                'maxletszam': foglalkozas.letszam,
                'tipus': foglalkozas.tipus,
                'nap': foglalkozas.nap,
                'mettol': timedelta2str(foglalkozas.mettol),
                'meddig': timedelta2str(foglalkozas.meddig),
                'tanar': foglalkozas.tanar,
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
    return f'{str(td.seconds//3600).zfill(2)}:{str(td.seconds//60%60).zfill(2)}'
