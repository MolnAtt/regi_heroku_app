# Generated by Django 3.2.6 on 2021-09-13 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0004_rename_vanmasik_foglalkozas_bomlik'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foglalkozas',
            name='masik_meddig',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='foglalkozas',
            name='masik_mettol',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='foglalkozas',
            name='masik_nev',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='foglalkozas',
            name='masik_tanar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='masik_tanar', to='APP.felhasznalo'),
        ),
    ]
