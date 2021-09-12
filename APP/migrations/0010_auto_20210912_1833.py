# Generated by Django 3.2.6 on 2021-09-12 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0009_auto_20210912_1703'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vezerlo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nev', models.CharField(max_length=100)),
                ('kod', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Vezerlő',
                'verbose_name_plural': 'Vezerlők',
            },
        ),
        migrations.AlterField(
            model_name='felhasznalo',
            name='felmentett',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='felhasznalo',
            name='gyogy',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='felhasznalo',
            name='kulsos',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='osztaly',
            name='nev',
            field=models.CharField(default='-', max_length=10),
        ),
    ]
