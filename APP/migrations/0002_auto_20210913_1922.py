# Generated by Django 3.2.6 on 2021-09-13 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foglalkozas',
            name='tipus',
            field=models.CharField(choices=[('dse', 'DSE'), ('nemdse', 'NEM DSE')], default='nemdse', max_length=10),
        ),
        migrations.DeleteModel(
            name='Tipus',
        ),
    ]
