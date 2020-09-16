from django.db import models
from django.core.validators import MinLengthValidator
from django.utils.timezone import now

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(
        max_length=50,
        validators= [MinLengthValidator(2, "Debe introducir dos caracteres")]
    )

    apellido = models.CharField(max_length=50
    )
    
    telefono = models.IntegerField(default=0)
    edad = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Tipos(models.Model):
    tipo_vuelo = models.CharField(
        max_length=50
        )

    def __str__(self):
        return f"{self.tipo_vuelo}"


class Clases(models.Model):
    clase = models.CharField(
        max_length=50
        )

    def __str__(self):
        return f"{self.clase}"


class Vuelo(models.Model):
    tipo_vuelo = models.ForeignKey(Tipos, on_delete=models.CASCADE)

    clase = models.ForeignKey(Clases, on_delete=models.CASCADE)

    origen = models.CharField(
        max_length=50,
        validators = [MinLengthValidator(2, "Debe introducir dos caracteres")]
    )

    destino = models.CharField(
        max_length=50,
        validators = [MinLengthValidator(2, "Debe introducir dos caracteres")]
    )  

    fecha_salida = models.DateTimeField('fecha de salida', default=now)
    
    fecha_regreso = models.DateTimeField('fecha de regreso', default=now)

    clientes = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.tipo_vuelo} {self.estado} {self.clase} {self.origen} {self.destino} {self.fecha_salida} {self.fecha_regreso}"