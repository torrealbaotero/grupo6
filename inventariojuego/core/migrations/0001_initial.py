# Generated by Django 5.0.4 on 2024-04-28 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('run', models.IntegerField(primary_key=True, serialize=False, verbose_name='run')),
                ('username', models.CharField(max_length=10, verbose_name='username')),
                ('nombres', models.CharField(max_length=60, verbose_name='nombres')),
                ('apellidos', models.CharField(max_length=60, verbose_name='apellidos')),
                ('contraseña', models.CharField(max_length=255, verbose_name='contraseña')),
                ('perfil', models.IntegerField(blank=True, null=True, verbose_name='perfil')),
            ],
        ),
    ]
