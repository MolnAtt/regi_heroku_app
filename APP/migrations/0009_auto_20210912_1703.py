# Generated by Django 3.2.6 on 2021-09-12 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0008_auto_20210912_1656'),
    ]

    operations = [
        migrations.AddField(
            model_name='felhasznalo',
            name='felmentett',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='felhasznalo',
            name='gyogy',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='felhasznalo',
            name='kulsos',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
