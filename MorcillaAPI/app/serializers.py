from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Empresa, Ciudad, Telefono


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class EmpresaSerializer(serializers.ModelSerializer):
    ciudades = serializers.StringRelatedField(many=True)

    class Meta:
        model = Empresa
        fields = ["id", 'nombre', 'CUIT',
                  'ciudades', 'cantidad_empleados', "logo"]


class TelefonoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telefono
        fields = ["id", 'numero']


class CiudadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        fields = ['id', 'nombre']
