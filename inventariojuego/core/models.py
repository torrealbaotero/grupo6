from django.db import models
from django.contrib.auth import get_user_model 
from django.conf import settings

# Create your models here.
class Usuario(models.Model):
    run= models.IntegerField(primary_key=True, verbose_name='run')
    username = models.CharField(max_length=10, verbose_name='username')
    nombres = models.CharField(max_length=60, verbose_name='nombres')
    apellidos = models.CharField(max_length=60, verbose_name='apellidos')
    password = models.CharField(max_length=255, verbose_name='contraseña')
    perfil = models.IntegerField(null=True, blank=True, verbose_name='perfil')

class Categoria(models.Model):
    id_categoria = models.IntegerField(primary_key=True, verbose_name='Id de la categoria')
    nombre_categoria = models.CharField(max_length=60, verbose_name='categoria')

    def __str__(self):
        return self.nombre_categoria
    
class Inventario(models.Model):
    id_inventario = models.IntegerField(primary_key=True, verbose_name='id_inventario')
    nombre = models.CharField(max_length=60, verbose_name='nombre')
    modelo = models.CharField(max_length=60, verbose_name='modelo')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='inventario/', null=True, verbose_name='Imagen del producto')

    def __str__(self):
        return self.nombre
    
class UserProfile(models.Model):
     user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
     role = models.CharField(max_length=20, choices=settings.ROLES) 

     def __str__(self):
         return self.user.username + ' - ' + self.role

