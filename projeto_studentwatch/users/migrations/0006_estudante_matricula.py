# Generated by Django 3.2.7 on 2021-10-12 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_remove_estudante_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudante',
            name='matricula',
            field=models.CharField(default='poioca', max_length=20),
        ),
    ]
