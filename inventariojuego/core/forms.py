from django import forms
from django.forms import ModelForm
from .models import Inventario

class InventarioForm(ModelForm):
    
    class Meta:
        model = Inventario
        fields = ['id_inventario','nombre','modelo','categoria','imagen']

