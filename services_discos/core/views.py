from django.shortcuts import render

# Importamos el Modelo=Tabla
from .models  import Discos
# Importamos el archivo serializers datos nativos
from .serializers import discos_serializer

# Importamos la restframework se encarga de convertir a JSON
from rest_framework import generics

from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.http.response import JsonResponse

#vista basada en clase
# class DiscosAllViewset(generics.ListAPIView):
#     #select * from discos
#     queryset = Discos.objects.all()
#     serializer_class = discos_serializer


@api_view(['GET','POST','DELETE'])  
def discos_all(request):
    #me permite traer la informacion de la BD
    if request.method == 'GET':
        discos = Discos.objects.all()
    #me permite insertar registros a la BD 
    elif request.method =='POST':
        #data que recibo que deseo insertar en la BD
        discos_data=JSONParser().parse(request)
        #convertirlo a datos nativos de PYTHON
        disco_serializer=discos_serializer(data=discos_data)
        if disco_serializer.is_valid():
            #lo almacena en la BD
            disco_serializer.save()
            return JsonResponse(disco_serializer.data,status=status.HTTP_201_CREATED)
        return  JsonResponse(disco_serializer.data,status=status.HTTP_400_BAD_REQUEST)   
    #mostrar todos los registros de la BD en JSON    
    Discos_serializer=discos_serializer(discos,many=True)    
    return JsonResponse(Discos_serializer.data,safe=False)
    
@api_view(['GET','PUT','DELETE'])
def discos_detail(request,pk):
    # para mostrar solo el registro que le pase como parametro
    disco=Discos.objects.get(pk=pk)
    if request.method =='GET':
        Disco_serializer=discos_serializer(disco)
        return JsonResponse(Disco_serializer.data)
    elif request.method == 'PUT':
        #todo obteniendo la data que deseo modificar
        disco_data=JSONParser().parse(request)
        #serializer es modificar en datos nativos PYTHON
        Disco_serializer=discos_serializer(disco,data=disco_data)
        if Disco_serializer.is_valid():
            #graba los cambios
            Disco_serializer.save()
            return JsonResponse(Disco_serializer.data)
        return JsonResponse(Disco_serializer.errors,status=status.HTTP_400_BAD_REQUEST)  
    elif request.method =='DELETE':
        disco.delete()
        return JsonResponse({'mensaje':'Disco Elimando Correctamente'},status=status.HTTP_204_NO_CONTENT)


        


    






    
