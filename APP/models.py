from django.db import models

class Bigyo(models.Model):

    szoveg = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Bigyo'
        verbose_name_plural = 'Bigyók'

    def __str__(self):
        return self.szoveg
