# Generated by Django 3.2.7 on 2021-10-31 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='presenca',
            options={'permissions': (('pode_registrar_presenca', 'Pode registrar presenca'),)},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
    ]
