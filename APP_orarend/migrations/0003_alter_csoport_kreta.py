# Generated by Django 3.2.6 on 2021-11-21 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP_orarend', '0002_alter_tantargy_hosszu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csoport',
            name='kreta',
            field=models.CharField(max_length=100),
        ),
    ]
