from django.db import models

class Empresas(models.Model):
    logo = models.CharField(max_length=100, null=True, blank=True)
    nombre = models.CharField(max_length=60, db_index=True)
    sede_principal = models.CharField(max_length=45)
    descripcion = models.TextField()
    sitio_web = models.URLField(max_length=200, null= True, blank=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

class Estrellas(models.Model):
    empresa = models.ForeignKey(Empresas, on_delete=models.CASCADE)
    estrella_1 = models.IntegerField(default=0)
    estrella_2 = models.IntegerField(default=0)
    estrella_3 = models.IntegerField(default=0)
    estrella_4 = models.IntegerField(default=0)
    estrella_5 = models.IntegerField(default=0)

class Valoraciones(models.Model):
    empresa = models.ForeignKey(Empresas, on_delete=models.CASCADE)
    puntualidad = models.IntegerField(default=0)
    seguridad = models.IntegerField(default=0)
    economica = models.IntegerField(default=0)
    amabilidad = models.IntegerField(default=0)
    caro = models.IntegerField(default=0)
    inseguro = models.IntegerField(default=0)
    impuntual = models.IntegerField(default=0)
    poco_amables = models.IntegerField(default=0)

class Usuarios(models.Model):
    foto_usuario = models.ImageField(upload_to='usuarios/', null=True, blank=True)
    nombre = models.CharField(max_length=45)
    email = models.EmailField(max_length=45, unique=True)
    contrasenia = models.CharField(max_length=100)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

class Comentarios(models.Model):
    empresa = models.ForeignKey(Empresas, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    comentario = models.TextField()

class Departamentos(models.Model):
    nombre = models.CharField(max_length=45)

    def __str__(self):
        return self.nombre

class Provincias(models.Model):
    departamento = models.ForeignKey(Departamentos, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=45)

    def __str__(self):
        return self.nombre

class Distritos(models.Model):
    provincia = models.ForeignKey(Provincias, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class AgenciasLima(models.Model):
    empresa = models.ForeignKey(Empresas, on_delete=models.CASCADE)
    distritos = models.ManyToManyField(Distritos, related_name='agencias')
    nombre_referencial = models.CharField(max_length=100)
    foto = models.CharField(max_length=100, null=True, blank=True)
    direccion = models.CharField(max_length=100)
    link_mapa = models.CharField(max_length=200)
    horario_de_atencion = models.CharField(max_length=45)
    telefono = models.CharField(max_length=20)
    cochera = models.BooleanField(null= True, blank=True)

    def __str__(self):
        return self.nombre_referencial
