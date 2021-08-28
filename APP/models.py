from django.db import models
from django.contrib.auth.models import User

class Felhasznalo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nev = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Felhasználó'
        verbose_name_plural = 'Felhasználók'

    def __str__(self):
        return str(self.user) + f' ({self.nev})'


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
    
    def jelentkezettek_szama(self) -> int:
        return -1

    def aktletszam(self) -> int:
        return Jelentkezes.objects.filter(foglalkozas = self).count()

    def lista(szurestipus) -> list:
        lista = []
        queryset = Foglalkozas.objects.all() if szurestipus=='' else Foglalkozas.objects.filter(tipus=Tipus.objects.get(kod=szurestipus))
        print(f"szurestipus: {szurestipus}")
        print(f"queryset: {queryset}")
        
        for foglalkozas in queryset:
            lista.append({
                'nev': foglalkozas.nev,
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
