from rest_framework import serializers
from .models import Citas,Publicacion,RegistroUsuarios,RegistroTatuadores


class CitasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Citas
        fields= "__all__"

class PublicacionSerializers(serializers.ModelSerializer):
    class Meta:
        model= Publicacion
        fields= "__all__"
       


# FORMULARIOS  REGISTROS

class RegistroUsuariosSerializers(serializers.ModelSerializer):
    class Meta:
        model= RegistroUsuarios
        fields= "__all__"

class RegistroTatuadoresSerializers(serializers.ModelSerializer):
    class Meta:
        model= RegistroTatuadores
        fields= "__all__"