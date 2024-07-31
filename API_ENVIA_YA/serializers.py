from rest_framework import serializers
from .models import Empresa, Usuario, Valoracion, Estrella, Comentario, AgenciaLima, Departamento, Distrito, Provincia


# Serializa la tabla Empresas
class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'
    # Solo campos específicos
class EmpresaDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = ['id', 'nombre', 'sede_principal', 'descripcion', 'sitio_web']


# Serializa la tabla valoracion
class ValoracionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Valoracion
        fields = '__all__'

    # Solo campos específicos
class ValoracionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Valoracion
        fields = ['id', 'puntualidad', 'seguridad', 'economica', 'caro', 'inseguro', 'impuntual', 'poco_amables']


# Serializa la tabla Estrellas
class EstrellasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Estrella
        fields = '__all__'

    # Solo campos específicos
class EstrellaDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estrella
        fields = ['id', 'estrella_1', 'estrella_2', 'estrella_3', 'estrella_4', 'estrella_5']

# Serializa la tabla Usuarios
class UsuarioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class UsuarioDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'foto_usuario', 'nombre', 'email']


# Serializa la tabla Comnetarios
class ComentariosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = '__all__'

class ComentariosDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = ['id', 'comentario']


# Serializa la tabla Agenciaslima
class AgenciasLimaSerializers(serializers.ModelSerializer):
    class Meta: 
        model = AgenciaLima
        fields = '__all__'

    # Solo campos específicos
class AgenciaslimaDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgenciaLima
        fields = ['id', 'nombre_referencial', 'direccion', 'link_mapa', 'horario_de_atencion', 'telefono', 'cochera']


# Serializa la tabla Departamentos
class DepartamentosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'


# Serializa la tabla Provincias
class ProvinciasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Provincia
        fields = '__all__'

class ProvinciasDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provincia
        fields = ['id', 'nombre']  # Solo campos específicos


# Serializa la tabla Distritos
class DistritosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Distrito
        fields = '__all__'

class DistritosDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distrito
        fields = ['id', 'nombre']  # Solo campos específicos