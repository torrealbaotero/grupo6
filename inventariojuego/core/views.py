from django.shortcuts import render, redirect
from .models import Usuario, Inventario, Categoria, UserProfile
from . forms import InventarioForm

#import requests

# Create your views here.
def login_usuario(request):
    if request.method == 'POST':
        username = request.POST.get('user')
        password = request.POST.get('pass')
        print("Datos del Form",username,password)
        #return render(request, 'core/login_usuario.html')
        usuarioBD = Usuario.objects.filter(username=username).first()
        print(usuarioBD)
        if usuarioBD is not None:
           if usuarioBD.password == password:
              if usuarioBD.perfil == 1:
                 print("Home Administrador")
                 return redirect('home')
              if usuarioBD.perfil == 2:
                 print("Home Usuario")
                 return redirect('home')
              else:
                 print("No se encontró perfil")
                 return render(request,'core/login_usuario.html')
           else:
             print("Password incorrecta")
             return render(request,'core/login_usuario.html')
        else:
          print("Usuario no existe")
          return render(request,'core/login_usuario.html')
    else:    
      return render(request,'core/login_usuario.html')
    
def home(request):
    inventarios = Inventario.objects.all()
    datos= {
        'inventario' : inventarios
    }
    print(datos)
    return render(request,'core/home.html',datos)

def form_inventario(request):
    datos = {
        'form': InventarioForm()
    }
    if request.method == 'POST':
        formulario = InventarioForm(request.POST, request.FILES)
        print("Contenido de request.FILES:", request.FILES)
        print("Contenido de request.POST:", request.POST)
        if formulario.is_valid():  
            formulario.save()
            datos['mensaje'] = "Guardado correctamente"
    return render(request, 'core/form_inventario.html', datos)


def form_mod_inventario(request, id):
    inventario = Inventario.objects.get(id_inventario=id)
    datos = {'form': InventarioForm(instance=inventario)}
    if request.method == 'POST':
        
        formulario = InventarioForm(request.POST, request.FILES, instance=inventario)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Modificado correctamente"
    return render(request, 'core/form_mod_inventario.html', datos)

def form_del_inventario(request, id):
    inventario = Inventario.objects.get(id_inventario=id)
    if request.method == 'POST':
        inventario.delete()
        # Redirigir a una página de éxito o a cualquier otra página deseada
        return redirect('/')
    return render(request, 'core/form_del_inventario.html', {'inventario': inventario})

def form_api(request):
   return render(request, 'core/form_api.html')

def form_api_back(request):
   url ="https://rawg.io/"
   responde =request.get(url)
   juegos = responde.json().get('results',[])

   context = {
      'juegos' : juegos
   }
   return render(request, 'core/form_api_back.html',context)
