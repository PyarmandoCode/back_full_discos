from rest_framework import serializers
from .models import Discos


# class discos_serializer(serializers.ModelSerializer):
#     class Meta:
#         model = Discos
#         fields = '__all__'



class discos_serializer(serializers.ModelSerializer):
    class Meta:
        model = Discos
        fields = ('id','titulo','descripcion','imagen','estado','precio','autor')

