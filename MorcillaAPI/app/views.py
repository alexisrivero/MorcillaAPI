from django.contrib.auth.models import User, Group
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework import permissions
from .models import Ciudad, Empresa, Telefono
from .serializers import CiudadSerializer, EmpresaSerializer, TelefonoSerializer, UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    #permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    #permission_classes = [permissions.IsAuthenticated]


class CiudadViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ciudades to be viewed or edited.
    """
    queryset = Ciudad.objects.all()
    serializer_class = CiudadSerializer
    #permission_classes = [permissions.IsAuthenticated]


class EmpresaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ciudades to be viewed or edited.
    """
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    #permission_classes = [permissions.IsAuthenticated]


class TelefonoViewset(viewsets.ModelViewSet):

    queryset = Telefono.objects.all()
    serializer_class = TelefonoSerializer
