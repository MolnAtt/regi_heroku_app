# Generated by Django 3.2.6 on 2021-08-28 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0006_tipus_kod'),
    ]

    operations = [
        migrations.AddField(
            model_name='foglalkozas',
            name='kod',
            field=models.CharField(default='lecserelendo', max_length=20),
            preserve_default=False,
        ),
    ]