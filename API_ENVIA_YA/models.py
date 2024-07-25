# models.py
from django.db import models

class Empresa(models.Model):
    Logo = models.CharField(max_length=200)
    Nombre = models.CharField(max_length=100)
    Sede_principal = models.CharField(max_length=100)
    Descripcion = models.TextField()
    Sitio_web = models.CharField(max_length=100)
    Created_ad = models.DateTimeField(auto_now_add=True)
    Updated_ad = models.DateTimeField(auto_now_add=True)

class Estrella(models.Model):
    Empresa_id = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    Estrella_1 = models.IntegerField()
    Estrella_2 = models.IntegerField()
    Estrella_3 = models.IntegerField()
    Estrella_4 = models.IntegerField()
    Estrella_5 = models.IntegerField()

class Valoracion(models.Model):
    Empresa_id = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    Puntualidad = models.IntegerField()
    Seguridad = models.IntegerField()
    Economica = models.IntegerField()
    Amabilidad = models.IntegerField()
    Caro = models.IntegerField()
    Inseguro = models.IntegerField()
    Impuntual = models.IntegerField()

class Usuario(models.Model):
    Foto_usuario = models.BinaryField(max_length=45)
    Nombre = models.CharField(max_length=100)
    Email = models.CharField(max_length=100, unique=True)
    Contrasena = models.CharField(max_length=20)
    Created_ad = models.DateTimeField(auto_now_add=True)
    Updated_ad = models.DateTimeField(auto_now_add=True)

class Comentario(models.Model):
    Empresa_id = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    Usuario_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    Fecha = models.DateTimeField()
    Comentario = models.TextField()

class AgenciaLima(models.Model):
    Empresa_id = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    Foto = models.BinaryField(max_length=200)
    Direccion = models.CharField(max_length=100)
    Horario_de_atencion = models.CharField(max_length=45)
    Telefono = models.IntegerField()
    Cochera = models.BooleanField()
    Salidas = models.TimeField()
    Llegadas = models.TimeField()

class Departamento(models.Model):
    Nombre = models.CharField(max_length=100)

class Provincia(models.Model):
    Departamento_id = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    Nombre = models.CharField(max_length=100)

class Distrito(models.Model):
    Provincia_id = models.ForeignKey(Provincia, on_delete=models.CASCADE)
    Agencia_lima_id = models.ForeignKey(AgenciaLima, on_delete=models.CASCADE)
    Nombre = models.CharField(max_length=100)

