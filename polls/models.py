from django.db import models


class Usuario(models.Model):
    idUsuario = models.IntegerField(primary_key=True)
    usuario = models.CharField(max_length=70)
    contraseña = models.CharField(max_length=70)

    def __str__(self):
        return self.idUsuario


class Root(models.Model):
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)


class Administrador(models.Model):
    usuario = models.ForeignKey('Usuario')
    DNI = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.IntegerField()
    fechaNacimiento = models.DateField()
    lugarNacimiento = models.CharField(max_length=100)
    direccionResidencia = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    idLibro = models.ForeignKey('Libro')
    idTienda = models.ForeignKey('Tienda')
    idMuro = models.ForeignKey('Muro')


class Cliente(models.Model):
    usuario = models.ForeignKey(Usuario)
    DNI = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.IntegerField()
    fechaNacimiento = models.DateField()
    lugarNacimiento = models.CharField(max_length=100)
    direccionResidencia = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    idLibro = models.ForeignKey('Libro')
    idTienda = models.ForeignKey('Tienda')
    idMuro = models.ForeignKey('Muro')
    numeroTarjeta = models.ForeignKey('Tarjeta')
    genero = models.CharField(max_length=100)
    temasPreferencia = models.CharField(max_length=300)


class Muro(models.Model):
    idMuro = models.IntegerField(primary_key=True)
    usuario = models.CharField(max_length=100)
    mensaje = models.CharField(max_length=500)
    tiempo = models.DateField()


class Tarjeta(models.Model):
    numeroTarjeta = models.IntegerField(primary_key=True)
    nombrePropietario = models.CharField(max_length=100)
    fechaCaducidad = models.DateField()
    cvv = models.IntegerField()


class TarjetaDebito(models.Model):
    numeroTarjeta = models.ForeignKey('Tarjeta')
    cupo = models.IntegerField()


class TarjetaCredito(models.Model):
    numeroTarjeta = models.ForeignKey('Tarjeta')
    cupo = models.IntegerField()