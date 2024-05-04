from django.contrib import admin
from .models import Usuario, Categoria, Inventario, UserProfile


# Register your models here.

admin.site.register(Usuario)
admin.site.register(Categoria)
admin.site.register(Inventario)#Revisar si hay que borrar
admin.site.register(UserProfile) 