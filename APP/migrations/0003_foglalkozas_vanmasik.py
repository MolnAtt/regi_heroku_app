# Generated by Django 3.2.6 on 2021-09-13 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0002_auto_20210913_1922'),
    ]

    operations = [
        migrations.AddField(
            model_name='foglalkozas',
            name='vanmasik',
            field=models.BooleanField(default=False),
        ),
    ]
