# Generated by Django 3.2.6 on 2021-08-28 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0005_rename_tipus_tipus_nev'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipus',
            name='kod',
            field=models.CharField(default='nemdse', max_length=8),
            preserve_default=False,
        ),
    ]