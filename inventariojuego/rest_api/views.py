from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response

from rest_framework.decorators import api_view

from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser

from rest_framework import status

from core.models import Inventario
from .serializers import InventarioSerializer

from core.models import Categoria
from .serializers import CategoriaSerializer

from rest_framework.decorators import permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def lista_inventario(request):
    if request.method == 'GET':
        inventario = Inventario.objects.all()
        serializer = InventarioSerializer(inventario,many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = InventarioSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            print('error',serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       
@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def lista_categoria(request):
    if request.method == 'GET':
        categoria = Categoria.objects.all()
        serializer = CategoriaSerializer(categoria, many=True)

        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CategoriaSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            print('error', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated,))
def vista_inventario(request, id_inventario):
    try:
        inventario = Inventario.objects.get(id_inventario=id_inventario)
    except Inventario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = InventarioSerializer(inventario)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = InventarioSerializer(inventario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        inventario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
