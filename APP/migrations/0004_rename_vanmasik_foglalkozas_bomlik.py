# Generated by Django 3.2.6 on 2021-09-13 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0003_foglalkozas_vanmasik'),
    ]

    operations = [
        migrations.RenameField(
            model_name='foglalkozas',
            old_name='vanmasik',
            new_name='bomlik',
        ),
    ]
