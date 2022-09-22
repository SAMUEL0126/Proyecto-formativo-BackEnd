from django.shortcuts import render
from rest_framework import viewsets
from .models import Citas,Publicacion,RegistroTatuadores,RegistroUsuarios
from .serializers import CitasSerializer,PublicacionSerializers,RegistroUsuariosSerializers,RegistroTatuadoresSerializers


class CitasViewsets(viewsets.ModelViewSet):
   queryset = Citas.objects.all()
   serializer_class = CitasSerializer

class PublicacionViewsets(viewsets.ModelViewSet):
    queryset=Publicacion.objects.all()
    serializer_class=PublicacionSerializers


class RegistroUsuarioViewsets(viewsets.ModelViewSet):
    queryset=RegistroUsuarios.objects.all()
    serializer_class=RegistroUsuariosSerializers

class RegistroTatuadoresViewsets(viewsets.ModelViewSet):
    queryset=RegistroTatuadores.objects.all()
    serializer_class=RegistroTatuadoresSerializers
