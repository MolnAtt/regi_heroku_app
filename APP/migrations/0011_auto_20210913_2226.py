# Generated by Django 3.2.6 on 2021-09-13 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0010_auto_20210913_2056'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Nap',
        ),
        migrations.AlterField(
            model_name='foglalkozas',
            name='egyik_nap',
            field=models.CharField(choices=[('hetfo', 'Hétfő'), ('kedd', 'Kedd'), ('szerda', 'Szerda'), ('csutortok', 'Csütörtök'), ('pentek', 'Péntek'), ('szombat', 'Szombat'), ('vasarnap', 'Vasárnap')], default='n.a.', max_length=10),
            preserve_default=False,
        ),
    ]
