from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=50)
    email=models.EmailField("Correo electronico",blank=True, null=True)
    telefono=models.CharField(max_length=12)

    # def __str__(self):
    #     return self.nombre, self.direccion

    # def __str__(self):

    #     return f' El nombre es: {self.nombre} la direccion es: {self.direccion} el email es: {self.email} el telefono es:{self.telefono}'

class Articulos(models.Model):
    nombre=models.CharField(max_length=50)
    seccion=models.CharField(max_length=50)
    precio=models.IntegerField()

class Pedidos(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()




