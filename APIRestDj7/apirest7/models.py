from django.db import models

class Proveedores(models.Model):

    
    nombres=models.CharField(max_length=30)
    apellidos=models.CharField(max_length=30)
    razonsocial=models.CharField(max_length=20)
    direccion=models.CharField(max_length=40)
    ruc=models.CharField(max_length=15)
    celular=models.CharField(max_length=20, null=True)
    wed=models.CharField(max_length=50)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now=True)

    class Meta:
        verbose_name = ("Proveedores")
        verbose_name_plural = ("Proveedoress")

    def __str__(self):
        return self.nombres

    

# Create your models here.
