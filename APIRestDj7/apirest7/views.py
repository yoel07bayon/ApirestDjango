from django.shortcuts import render

from rest_framework import viewsets
from .serializers import ProveedoresSerializer
from .models import Proveedores

class ProveedoresViewSet(viewsets.ModelViewSet):
    queryset=Proveedores.objects.all();
    serializer_class=ProveedoresSerializer


# Create your views here.
