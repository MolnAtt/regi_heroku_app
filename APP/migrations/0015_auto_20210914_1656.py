# Generated by Django 3.2.6 on 2021-09-14 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0014_auto_20210914_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foglalkozas',
            name='egyik_nap',
            field=models.CharField(choices=[('Hétfő', 'Hétfő'), ('Kedd', 'Kedd'), ('Szerda', 'Szerda'), ('Csütörtök', 'Csütörtök'), ('Péntek', 'Péntek'), ('Szombat', 'Szombat'), ('Vasárnap', 'Vasárnap')], max_length=10),
        ),
        migrations.AlterField(
            model_name='foglalkozas',
            name='masik_nap',
            field=models.CharField(blank=True, choices=[('Hétfő', 'Hétfő'), ('Kedd', 'Kedd'), ('Szerda', 'Szerda'), ('Csütörtök', 'Csütörtök'), ('Péntek', 'Péntek'), ('Szombat', 'Szombat'), ('Vasárnap', 'Vasárnap')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='osztaly',
            name='kod',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='osztaly',
            name='nev',
            field=models.CharField(default='-', max_length=50),
        ),
    ]
