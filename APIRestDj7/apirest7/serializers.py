from rest_framework import serializers
from .models import Proveedores

class ProveedoresSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Proveedores
        fields=['nombres', 'apellidos', 'razonsocial', 'direccion','ruc','celular','wed']