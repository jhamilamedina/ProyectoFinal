from django.db import models

class Empresa(models.Model):
    logo = models.ImageField(upload_to='logos/', null=True, blank=True)
    nombre = models.CharField(max_length=100, db_index=True)
    sede_principal = models.CharField(max_length=100)
    descripcion = models.TextField()
    sitio_web = models.URLField(max_length=200)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

class Estrella(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    estrella_1 = models.IntegerField()
    estrella_2 = models.IntegerField()
    estrella_3 = models.IntegerField()
    estrella_4 = models.IntegerField()
    estrella_5 = models.IntegerField()

class Valoracion(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    puntualidad = models.IntegerField()
    seguridad = models.IntegerField()
    economica = models.IntegerField()
    amabilidad = models.IntegerField()
    caro = models.IntegerField()
    inseguro = models.IntegerField()
    impuntual = models.IntegerField()
    poco_amables = models.IntegerField()

class Usuario(models.Model):
    foto_usuario = models.ImageField(upload_to='usuarios/', null=True, blank=True)
    nombre = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    contrasenia = models.CharField(max_length=20)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

class Comentario(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    comentario = models.TextField()

class Departamento(models.Model):
    nombre = models.CharField(max_length=100)

class Provincia(models.Model):
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)

class Distrito(models.Model):
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)

class AgenciaLima(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    distrito = models.ForeignKey(Distrito, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='agencias/', null=True, blank=True)
    nombre_referencial = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    link_mapa = models.CharField(max_length=200)
    horario_de_atencion = models.CharField(max_length=45)
    telefono = models.CharField(max_length=20)
    cochera = models.BooleanField()
