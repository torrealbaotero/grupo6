from django.urls import path
from . import views

urlpatterns = [
    path('inventario/', views.lista_inventario,name="lista_inventario"),
    path('categoria/', views.lista_categoria,name="lista_categoria"),    
    path('inventario/<id_inventario>', views.vista_inventario,name="vista_inventario"),    
]